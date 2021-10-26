from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    text = serializers.CharField(max_length=100)

    class Meta:
        fields = '__all__'
        model = Message
