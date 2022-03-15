from django.views.generic import ListView
from kalevent.models import Event

class AllEventsListView(ListView):

    template_name = 'kalevent/events_list.html'
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)

class RunningEventsListView(ListView):

    template_name = 'kalevent/events_list.html'
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)