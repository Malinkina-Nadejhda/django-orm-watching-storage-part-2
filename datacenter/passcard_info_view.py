from datacenter.models import Visit, Passcard, get_duration, format_duration, if_visit_long
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        is_strange = if_visit_long(duration, minutes=60)
        passcard_info = {
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
            'is_strange': is_strange
        }
        this_passcard_visits.append(passcard_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


