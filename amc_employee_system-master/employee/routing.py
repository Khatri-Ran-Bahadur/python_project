from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/chat/Job_Chat_Box/',consumers.ChatConsumer),
]

