from rest_framework import serializers 
from .models import Genre


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class GenresNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name']