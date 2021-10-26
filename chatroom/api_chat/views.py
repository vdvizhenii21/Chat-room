from rest_framework import viewsets
from .models import Message
from rest_framework.permissions import AllowAny
from .serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    http_method_names = 'get', 'post'
    permission_classes = [AllowAny]
