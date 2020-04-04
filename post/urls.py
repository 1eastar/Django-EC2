from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import EssayViewSet, AlbumViewSet, FileViewSet

router = DefaultRouter()
router.register('essay', EssayViewSet)
router.register('album', AlbumViewSet)
router.register('file', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
