from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Event, EventForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from collections import defaultdict
from django.shortcuts import render
from .models import Event
import calendar
from datetime import datetime

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'pages/event_create.html'
    success_url = 'all'  # Redirect after a successful submission

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EventListView(ListView):
    
    def all_events(request):
        events = Event.objects.all().order_by('date')  # Get all events ordered by date
        return render(request, 'pages/all_events.html', {'events': events})
    
    def event_detail(request, event_id):
        event = get_object_or_404(Event, id=event_id)  # Get the event or 404 if not found
        return render(request, 'pages/event_detail.html', {'event': event})
   

class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'location','related_course', 'event_type']
    template_name = 'events/update_event.html'
   #permission_required = 'events.change_event'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.groups.filter(name='Instructors').exists():
            queryset = queryset.filter(created_by=self.request.user)
        return queryset

    def form_valid(self, form):
        if 'event_type' in form.changed_data and not self.request.user.groups.filter(name='Instructors').exists():
            form.add_error('event_type', 'You are not permitted to change the event type.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
    def edit_event(request, event_id):
        event = get_object_or_404(Event, id=event_id)
        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('event_detail', event_id=event.id)
        else:
            form = EventForm(instance=event)
        return render(request, 'pages/edit_event.html', {'form': form})
    
class EventDeleteView(DeleteView):

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.groups.filter(name='Instructors').exists():
            queryset = queryset.filter(created_by=self.request.user)
        return queryset
    
    
    def delete_event(request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event.delete()

        if request.user.groups.filter(name='student').exists():
            return redirect('all_student_events')
        
        if request.user.groups.filter(name='teacher').exists():
            return redirect('all_teacher_events')

from django.shortcuts import render
from .models import Event
import calendar
from datetime import datetime

from collections import defaultdict
from datetime import datetime
import calendar
from django.shortcuts import render
from .models import Event

def calendar_view(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    year = int(request.GET.get('year', current_year))
    month = int(request.GET.get('month', current_month))

    # Set the first day of the week to Sunday
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)

    month_calendar = c.monthdayscalendar(year, month)
    events = Event.objects.filter(date__year=year, date__month=month)

    events_by_date = defaultdict(list)
    for event in events:
        events_by_date[event.date.day].append(event)

    new_calendar = []
    for week in month_calendar:
        new_week = []
        for day in week:
            if day != 0:
                day_events = events_by_date.get(day, [])
                new_week.append((day, day_events))
            else:
                new_week.append((" ", []))
        new_calendar.append(new_week)

    years = range(2020, 2031)  # Years for the dropdown
    months = range(1, 13)      # Months for the dropdown

    context = {
        'calendar': new_calendar,
        'month': month,
        'year': year,
        'years': years,
        'months': months
    }
    return render(request, 'calendar.html', context)


