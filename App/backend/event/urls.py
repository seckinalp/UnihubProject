from django.urls import path
from .views import calendar_view, EventListView

urlpatterns = [
    path('calendar/', calendar_view, name='calendar'),
    path('event/<int:event_id>/', EventListView.event_detail, name='event_detail'),
]
