from rest_framework import serializers

from .models import Number, Message


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = (
            'pk',
            'number',
        )
        read_only_fields = (
            'pk',
            'number',
        )


class MessageSerializer(serializers.ModelSerializer):
    number = NumberSerializer(read_only=True)

    class Meta:
        model = Message
        fields = (
            'pk',
            'number',
            'message',
        )
        read_only_fields = (
            'pk',
            'number',
        )
