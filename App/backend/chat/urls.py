from django.urls import path
from .views import chat_view, fetch_messages
from .views import delete_message

urlpatterns = [
    path('chat/', chat_view, name='chat_base'),
    path('chat/<str:username>/', chat_view, name='chat_with_user'),
    path('chat/<str:username>/fetch/', fetch_messages, name='fetch_messages'),
     path('chat/delete_message/<int:message_id>/', delete_message, name='delete_message'),
]

