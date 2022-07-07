from rest_framework import serializers
from .models import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['creation_date', 'done', 'id']


class ListTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['id']


class ChangeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['id']
        extra_kwargs = {
            'creation_date': {'read_only': True},
        }
