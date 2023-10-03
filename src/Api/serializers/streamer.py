# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from rest_framework import serializers

# Athena Packages

# Local Imports
from Api.models.streamer import Streamer

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StreamerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Streamer
        fields = '__all__'