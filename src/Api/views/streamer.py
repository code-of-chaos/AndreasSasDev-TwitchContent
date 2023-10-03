# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from rest_framework import viewsets

# Athena Packages

# Local Imports
from Api.models.streamer import Streamer
from Api.serializers.streamer import StreamerSerializer

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StreamerViewSet(viewsets.ModelViewSet):
    queryset = Streamer.objects.all()
    serializer_class = StreamerSerializer
