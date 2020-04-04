from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, renderers
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Essay, Album, File
from .serializer import EssaySerializer, AlbumSerializer, FileSerializer
from .pagination import EssayPagination


class EssayViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    queryset = Essay.objects.all().order_by('id')
    serializer_class = EssaySerializer
    pagination_class = EssayPagination

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',)

    def get_queryset(self):
        print(self.request.auth)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    filter_backends = [SearchFilter]
    search_flelds = ('desc',)

    def get_queryset(self):

        return super().get_queryset()


class FileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = File.objects.all()
    serializer_class = FileSerializer

    filter_backends = [SearchFilter]
    search_flelds = ('desc',)

    def get_queryset(self):

        return super().get_queryset()