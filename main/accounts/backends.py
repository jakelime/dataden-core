from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from typing import Optional

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(
        self,
        request,
        username: Optional[str] = None,
        password: str = "",
        **kwargs,
    ):
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=username)
            except Exception:
                return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
