from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import modelGroup
from .serializers import GroupSerializer

@api_view(['POST'])
def set_group(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_group(request):
    chat_id = request.query_params.get('chatId')
    if chat_id:
        try:
            group_id = modelGroup.objects.get(chatId=chat_id).groupId
            return Response({'groupId': group_id}, status=status.HTTP_200_OK)
        except modelGroup.DoesNotExist:
            return Response({'error': 'ChatId not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'ChatId parameter is required'}, status=status.HTTP_400_BAD_REQUEST)