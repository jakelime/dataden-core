# api/serializers.py
from rest_framework import serializers
from .models import Item  # Import the Item model


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for the Item model."""

    class Meta:
        model = Item
        # Specify the fields to include in the serialized output
        fields = ["id", "name", "description", "created_at"]
        # Specify fields that should only be read (not required during creation/update)
        read_only_fields = ["id", "created_at"]
