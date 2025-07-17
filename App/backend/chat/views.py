from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

def chat_view(request, username=None):
    current_user = request.user
    if not current_user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated

    users = User.objects.exclude(id=current_user.id)
    selected_user = User.objects.filter(username=username).first()

    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            message_text = request.POST.get('message')
            if selected_user:
                Message.objects.create(sender=current_user, recipient=selected_user, message=message_text)
                return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'User not found'})
        else:
            form = MessageForm(request.POST)
            if form.is_valid():
                new_message = form.save(commit=False)
                new_message.sender = current_user
                new_message.recipient = selected_user
                new_message.save()
                return redirect('chat_with_user', username=selected_user.username)
    else:
        form = MessageForm()

    messages = Message.objects.filter(
        (Q(sender=current_user) & Q(recipient=selected_user)) |
        (Q(sender=selected_user) & Q(recipient=current_user))
    ).order_by('timestamp') if selected_user else Message.objects.none()

    return render(request, 'chat/chat_room.html', {
        'users': users,
        'selected_user': selected_user,
        'messages': messages,
        'form': form
    })
# views.py
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Message
import datetime

User = get_user_model()

def fetch_messages(request, username):
    selected_user = User.objects.filter(username=username).first()
    if not selected_user:
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)

    last_refresh = request.GET.get('last_refresh')
    if last_refresh:
        last_refresh = datetime.datetime.strptime(last_refresh, "%Y-%m-%dT%H:%M:%S.%fZ")

    messages = Message.objects.filter(
        (Q(sender=request.user, recipient=selected_user) | Q(recipient=request.user, sender=selected_user)),
        timestamp__gt=last_refresh
    ).order_by('timestamp')

    messages_data = [
        {'sender': message.sender.username, 'message': message.message, 'timestamp': message.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ')}
        for message in messages
    ]

    return JsonResponse({'status': 'success', 'messages': messages_data})

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Message

@require_POST
@csrf_exempt
def delete_message(request, message_id):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'error', 'error': 'Authentication required'}, status=403)

    message = Message.objects.filter(id=message_id, sender=request.user).first()
    if not message:
        return JsonResponse({'status': 'error', 'error': 'Message not found or access denied'}, status=404)

    message.delete()
    return JsonResponse({'status': 'success'})
