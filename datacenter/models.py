from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


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

