# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models

# Athena Packages

# Local Imports
from Api.models.streamer import Streamer

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class StreamInfo(models.Model):
    streamer = models.ForeignKey(Streamer, on_delete=models.PROTECT, null=False)

    timestamp= models.DateTimeField()
    subject_name = models.CharField(max_length=140)