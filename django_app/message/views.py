from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

from .serializers import NumberSerializer, MessageSerializer
from .models import Number


# Create your views here.
class CreateNumberAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        last = Number.objects.last()
        if last:
            number = last.number + 1
        else:
            number = 0

        num_obj = Number.objects.create(number=number)

        serializer = NumberSerializer(data={'number': num_obj.number})
        if serializer.is_valid():
            return Response(data=serializer.data)


class MessageSendAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)