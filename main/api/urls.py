# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Import views from the current directory

# Create a router instance
router = DefaultRouter()

# Register the ItemViewSet with the router.
# 'items' will be the URL prefix (e.g., /api/items/)
# 'item' is the base name used for generating URL names.
router.register(r"items", views.ItemViewSet, basename="item")

# The API URLs are now determined automatically by the router.
# We include the generated URLs in our urlpatterns.
urlpatterns = [
    path("", include(router.urls)),
]
