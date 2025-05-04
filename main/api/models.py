from django.db import models

# Create your models here.


class Item(models.Model):
    """Represents an item in our simple API."""

    name = models.CharField(max_length=100, help_text="Name of the item")
    description = models.TextField(
        blank=True, null=True, help_text="Optional description"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when the item was created"
    )

    def __str__(self):
        """String representation of the Item model."""
        return self.name

    class Meta:
        ordering = ["-created_at"]  # Default ordering for queries
