from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import modelGroup

class modelGroupAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_set_data(self):
        data = {"chatId": "test_chatId", "groupId": "test_groupId", "degree": "bachelor", "studyForm": "full-time", "course": 1}
        response = self.client.post('/api/set_data/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(modelGroup.objects.filter(chatId='test_chatId').exists())

    def test_get_group(self):
        modelGroup.objects.create(chatId='test_chatId', groupId='test_groupId')
        response = self.client.get('/api/get_group/?chatId=test_chatId')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['groupId'], 'test_groupId')

    def test_get_data_invalid_chatId(self):
        response = self.client.get('/api/get_group/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_group_not_found(self):
        response = self.client.get('/api/get_group/?chatId=non_existing_chatId')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
