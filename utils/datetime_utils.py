from datetime import datetime, date, timedelta
from django.utils.translation import ugettext as _

from decimal import Decimal
import pdb
from operator import itemgetter
import calendar


def get_today():
    return date.today()


def get_now():
    return datetime.now()


def get_delta_by_hours(h):
    return timedelta(seconds=int(Decimal(h) * 3600))


def get_day_of_week(date_time_object, in_words=False):
    WEEK_CHOICES = (
        (0, _('Monday')),
        (1, _('Tuesday')),
        (2, _('Wednesday')),
        (3, _('Thursday')),
        (4, _('Friday')),
        (5, _('Saturday')),
        (6, _('Sunday')),
    )
    if in_words:
        return WEEK_CHOICES[date_time_object.weekday()][1]
    else:
        return date_time_object.weekday()


def date_from_string(date_str, format_str):
    """
    returns a date object by a string
    """
    return datetime.strptime(date_str, format_str).date()


def string_from_date(date, format_str):
    return datetime.strftime(date, format_str)
