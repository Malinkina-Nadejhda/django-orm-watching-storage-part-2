from django.utils import timezone


def get_duration(visit):
    local_time = timezone.localtime()
    entered_time = timezone.localtime(visit.entered_at)
    if visit.leaved_at:
        leaved_time = timezone.localtime(visit.leaved_at)
        visit_time = leaved_time - entered_time
    else:
        visit_time = local_time - entered_time
    duration = int(visit_time.total_seconds())
    return duration


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    formatted_duration = f"{hours:02d}ч {minutes:02d}мин {seconds:02d}сек"
    return formatted_duration


def is_visit_long(duration, minutes=60):
    long_visit = duration > minutes * 60
    return long_visit

