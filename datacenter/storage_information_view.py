from datacenter.models import Visit
from django.shortcuts import render
from time_helpers import get_duration, format_duration

def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in active_visits:
        duration_seconds = get_duration(visit)
        formatted_duration = format_duration(duration_seconds)
        visit_data = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
        }
        non_closed_visits.append(visit_data)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

