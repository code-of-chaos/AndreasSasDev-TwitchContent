# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from rest_framework import viewsets

# Athena Packages

# Local Imports
from Api.models.stream_info import StreamInfo
from Api.models.streamer import Streamer
from Api.serializers.stream_info import StreamInfoSerializer

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StreamInfoViewSet(viewsets.ModelViewSet):
    queryset = StreamInfo.objects.all()
    serializer_class = StreamInfoSerializer

    def get_queryset(self):
        return StreamInfo.objects.filter(streamer=self.kwargs['streamer_pk'])
        # return StreamInfo.objects.filter(streamer=Streamer.objects.get(id=self.kwargs['streamer_pk']))