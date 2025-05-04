# api/views.py
from django.shortcuts import render
from rest_framework import permissions, viewsets  # Import permissions if needed later

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Items to be viewed or edited.
    Provides list, create, retrieve, update, partial_update, destroy actions.
    """

    queryset = Item.objects.all()  # The default set of objects for this view
    serializer_class = ItemSerializer  # The serializer to use for this view
    # Optional: Add permissions (e.g., only allow authenticated users)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
