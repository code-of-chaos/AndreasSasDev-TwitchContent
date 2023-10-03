# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from rest_framework import serializers

# Athena Packages

# Local Imports
from Api.models.stream_info import StreamInfo

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StreamInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamInfo
        fields = '__all__'