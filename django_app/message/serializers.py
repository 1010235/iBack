from rest_framework import serializers

from .models import Number, Message


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = (
            'number',
        )


class MessageSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(source='number.number')

    class Meta:
        model = Message
        fields = (
            'pk',
            'number',
            'msg',
        )
        read_only_fields = (
            'pk',
            'number',
        )

    def save(self, **kwargs):
        num_obj = Number.objects.filter(number=self.initial_data.get('number'))
        if not num_obj.exists():
            raise serializers.ValidationError("Number is not exist.")
        num_obj = num_obj[0]
        instance = super().save(number=num_obj, **kwargs)

        return instance.save()
