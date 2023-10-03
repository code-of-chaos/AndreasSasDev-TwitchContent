# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.urls import include, path
from rest_framework_nested import routers

# Athena Packages

# Local Imports
import Api.views as ApiViews

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# Create  Default router
router = routers.DefaultRouter()
router.register(r'streamers', ApiViews.StreamerViewSet)

# Create Nested router for "streamers"
streamer_router = routers.NestedSimpleRouter(router,r'streamers', lookup="streamer")
streamer_router.register(r'stream-info', ApiViews.StreamInfoViewSet)
# streamer_router.register(r'stream-info/latest', ApiViews.LatestStreamInfoViewSet)

# Wire the router to url
urlpatterns = [
    path('', include(router.urls)),
    path('', include(streamer_router.urls)),
    path("streamer/<int:streamer_pk>/stream-info/latest/", ApiViews.LatestStreamInfoViewSet.as_view()),
]