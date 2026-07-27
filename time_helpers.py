from django.utils import timezone


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


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
    hours = duration // SECONDS_IN_HOUR
    minutes = (duration % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    seconds = duration % SECONDS_IN_MINUTE
    formatted_duration = f"{hours:02d}ч {minutes:02d}мин {seconds:02d}сек"
    return formatted_duration


def is_visit_long(duration, minutes=60):
    long_visit = duration > minutes * SECONDS_IN_MINUTE
    return long_visit

