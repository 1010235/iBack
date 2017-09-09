from django.shortcuts import render
from rest_framework import views, serializers, exceptions
from rest_framework.response import Response

from .serializers import NumberSerializer, MessageSerializer
from .models import Number, Message


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


class MessageListAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            number = Number.objects.get(number=kwargs.get('number'))
            query = number.message_set.all()
            serializer = MessageSerializer(query, many=True)
            change_unread_to_read(query)

            return Response(serializer.data)
        except Number.DoesNotExist:
            raise exceptions.NotFound('Number is not exists')


class MessageNewListAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            number = Number.objects.get(number=kwargs.get('number'))
            serializer = MessageSerializer(number.message_set.filter(is_read=False), many=True)

            return Response(serializer.data)
        except Number.DoesNotExist:
            raise exceptions.NotFound('Number is not exists')


def change_unread_to_read(query):
    for i in query:
        i.is_read = True
        i.save()
