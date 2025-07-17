from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def get_default_sender():
    # Returns the first user's ID in the system
    return User.objects.first().id

def get_default_recipient():
    # Returns the first user's ID in the system
    return User.objects.first().id
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, default=get_default_sender)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE, default=get_default_recipient)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'From {self.sender} to {self.recipient}: {self.message}'
    
