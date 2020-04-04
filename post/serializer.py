from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Essay, Album, File

class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='auth.username')
    class Meta:
        model = Essay
        fields = ['pk','title','body','author_name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'