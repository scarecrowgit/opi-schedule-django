from rest_framework import serializers
from .models import modelGroup

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelGroup
        fields = ['chatId', 'groupId']
