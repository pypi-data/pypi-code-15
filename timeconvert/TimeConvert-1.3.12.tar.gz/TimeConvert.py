# -*- coding: utf-8 -*-

from __future__ import division

import datetime
import time

import pytz


# In [40]: import pytz
# In [41]: pytz.all_timezones


class TimeConvert:
    def __init__(self, timezone=None, format=None):
        self.TIME_ZONE = timezone or 'Asia/Shanghai'
        self.TIME_FORMAT = format or '%Y-%m-%d %H:%M:%S'

    def timezone(self, timezone=None):
        return timezone or self.TIME_ZONE

    def format(self, format=None):
        return format or self.TIME_FORMAT

    # PRIVATE

    def __utc_datetime(self, utc_dt=None):
        return utc_dt or self.utc_datetime()

    def __local_datetime(self, local_dt=None):
        return local_dt or self.local_datetime()

    def __datetime(self, dt=None, utc=True):
        return dt or (self.utc_datetime() if utc else self.local_datetime())

    def __remove_ms_or_not(self, dt=None, ms=True):
        return dt if ms else self.remove_microsecond(dt)

    # OFFSET

    def offset(self):
        now_timestamp = time.time()
        return datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)

    # VALIDATE

    def validate_string(self, string, format=None):
        if not string:
            return False
        try:
            time.strptime(string, self.format(format))
        except ValueError:
            return False
        return True

    # REPLACE

    def remove_microsecond(self, dt):
        return dt.replace(microsecond=0) if hasattr(dt, 'replace') else dt

    # DATETIME

    def utc_datetime(self, ms=True):
        return self.__remove_ms_or_not(datetime.datetime.utcnow().replace(tzinfo=pytz.utc), ms=ms)

    def local_datetime(self, ms=True, timezone=None):
        return self.__remove_ms_or_not(self.to_local_datetime(self.utc_datetime(), self.timezone(timezone)), ms=ms)

    def is_utc_datetime(self, dt):
        return dt.tzinfo == pytz.utc

    def is_local_datetime(self, dt, local_tz=None):
        # In [100]: pytz.timezone('Asia/Shanghai')
        # Out[100]: <DstTzInfo 'Asia/Shanghai' LMT+8:06:00 STD>

        # In [101]: tc.local_datetime().tzinfo
        # Out[101]: <DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>

        # In [102]: pytz.timezone('Asia/Shanghai') == tc.local_datetime().tzinfo
        # Out[102]: False

        # In [103]: str(pytz.timezone('Asia/Shanghai')) == str(tc.local_datetime().tzinfo)
        # Out[103]: True

        return str(dt.tzinfo) == str(local_tz)

    def to_utc_datetime(self, dt, timezone=None):
        if self.is_utc_datetime(dt):
            return dt
        try:
            dt = self.make_naive(dt)
        except ValueError:
            pass
        local_tz = pytz.timezone(self.timezone(timezone))
        local_dt = local_tz.localize(dt, is_dst=None)
        return local_dt.astimezone(pytz.utc)

    def to_local_datetime(self, dt, timezone=None):
        tzname = self.timezone(timezone)
        if self.is_local_datetime(dt, local_tz=tzname):
            return dt
        local_tz = pytz.timezone(tzname)
        utc_dt = dt.replace(tzinfo=pytz.utc)
        return utc_dt.astimezone(local_tz)

    def yesterday_utc_datetime(self, ms=True):
        return self.__remove_ms_or_not(self.several_days_ago(self.utc_datetime(), days=1), ms=ms)

    def tomorrow_utc_datetime(self, ms=True):
        return self.__remove_ms_or_not(self.several_days_coming(self.utc_datetime(), days=1), ms=ms)

    def yesterday_local_datetime(self, ms=True, timezone=None):
        return self.__remove_ms_or_not(self.several_days_ago(self.local_datetime(timezone=self.timezone(timezone)), days=1), ms=ms)

    def tomorrow_local_datetime(self, ms=True, timezone=None):
        return self.__remove_ms_or_not(self.several_days_coming(self.local_datetime(timezone=self.timezone(timezone)), days=1), ms=ms)

    def several_days_ago(self, dt=None, utc=True, days=0):
        return self.__datetime(dt, utc) - datetime.timedelta(days=days)

    def several_days_coming(self, dt=None, utc=True, days=0):
        return self.__datetime(dt, utc) + datetime.timedelta(days=days)

    def several_time_ago(self, dt=None, utc=True, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        return self.__datetime(dt, utc) - datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)

    def several_time_coming(self, dt=None, utc=True, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        return self.__datetime(dt, utc) + datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)

    # STRING

    def utc_string(self, utc_dt=None, format=None):
        return self.datetime_to_string(self.__utc_datetime(utc_dt), self.format(format))

    def local_string(self, local_dt=None, format=None):
        return self.datetime_to_string(self.__local_datetime(local_dt), self.format(format))

    def datetime_to_string(self, dt, format=None):
        return dt.strftime(self.format(format))

    # TIMESTAMP

    def utc_timestamp(self, utc_dt=None, ms=False):
        return self.datetime_to_timestamp(self.__utc_datetime(utc_dt), ms=ms)

    def local_timestamp(self, local_dt=None, ms=False):
        return self.datetime_to_timestamp(self.__local_datetime(local_dt), ms=ms)

    def datetime_to_timestamp(self, dt, ms=False):
        # http://stackoverflow.com/questions/26161156/python-converting-string-to-timestamp-with-microseconds
        # ``dt - epoch`` will raise ``TypeError: can't subtract offset-naive and offset-aware datetimes``
        # Total seconds from ``1970-01-01 00:00:00``(utc or local)
        # Different from definition of timestamp(时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数)
        stamp = self.structime_to_timestamp(dt.timetuple())
        if not ms:
            return stamp
        return stamp + dt.microsecond / 10 ** 6

    def structime_to_timestamp(self, structime):
        return int(time.mktime(structime))

    # STRING ==> DATETIME

    def string_to_utc_datetime(self, string, format=None):
        format = self.format(format)
        if not self.validate_string(string, format):
            return None
        return self.to_utc_datetime(self.string_to_local_datetime(string, format))

    def string_to_local_datetime(self, string, format=None):
        format = self.format(format)
        if not self.validate_string(string, format):
            return None
        return datetime.datetime.strptime(string, format)

    def utc_string_to_utc_datetime(self, utc_string, format=None):
        format = self.format(format)
        if not self.validate_string(utc_string, format):
            return None
        return self.to_utc_datetime(self.string_to_local_datetime(utc_string, format)) + self.offset()

    # STRING ==> TIMESTAMP

    def string_to_timestamp(self, string, format=None, ms=False):
        return self.string_to_local_timestamp(string, format, ms=ms)

    def string_to_utc_timestamp(self, string, format=None, ms=False):
        format = self.format(format)
        if not self.validate_string(string, format):
            return None
        return self.datetime_to_timestamp(self.string_to_utc_datetime(string, format), ms=ms)

    def string_to_local_timestamp(self, string, format=None, ms=False):
        format = self.format(format)
        if not self.validate_string(string, format):
            return None
        return self.datetime_to_timestamp(self.string_to_local_datetime(string, format), ms=ms)

    # TIME_DELTA

    def timestamp_delta(self, stamp1, stamp2, interval=None):
        delta = stamp1 - stamp2
        abs_delta = abs(delta)
        sign = abs_delta and delta // abs_delta
        delta_seconds = abs_delta % 60
        delta_minutes = abs_delta // 60 % 60
        delta_hours = abs_delta // 3600 % 24
        delta_days = abs_delta // 86400
        delta_weeks = abs_delta // 604800
        return {
            'sign': sign,
            'weeks': delta_weeks,
            'days': delta_days,
            'hours': delta_hours,
            'minutes': delta_minutes,
            'seconds': delta_seconds,
            'total_seconds': abs_delta,
            'delta': delta,
            'count_down_seconds': abs(min(delta, 0)),
            'interval': interval and abs_delta >= interval
        }

    def datetime_delta(self, dt1, dt2, interval=None):
        return self.timestamp_delta(self.datetime_to_timestamp(dt1), self.datetime_to_timestamp(dt2), interval)

    def string_delta(self, string1, string2, interval=None, format=None, format1='', format2=''):
        format = self.format(format)
        if (not self.validate_string(string1, format1 or format)) or (not self.validate_string(string2, format2 or format)):
            return None
        return self.timestamp_delta(self.string_to_timestamp(string1, format1 or format), self.string_to_timestamp(string2, format2 or format), interval)

    # TIME_COUNT_DOWN

    def timestamp_countdown(self, stamp):
        return abs(min((self.utc_timestamp() - stamp), 0))

    def datetime_countdown(self, dt):
        return self.timestamp_countdown(self.datetime_to_timestamp(dt))

    def string_countdown(self, string, format=None):
        format = self.format(format)
        if not self.validate_string(string, format):
            return None
        return self.timestamp_countdown(self.string_to_timestamp(string, format))

    # MIDNIGHT

    def utc_datetime_midnight(self, utc_dt=None):
        return (self.__utc_datetime(utc_dt)).replace(hour=0, minute=0, second=0, microsecond=0)

    def utc_seconds_since_midnight(self, utc_dt=None):
        utc_dt = self.__utc_datetime(utc_dt)
        return self.total_seconds(utc_dt - self.utc_datetime_midnight(utc_dt))

    def local_datetime_midnight(self, local_dt=None):
        return (self.__local_datetime(local_dt)).replace(hour=0, minute=0, second=0, microsecond=0)

    def local_seconds_since_midnight(self, local_dt=None):
        local_dt = self.__local_datetime(local_dt)
        return self.total_seconds(local_dt - self.local_datetime_midnight(local_dt))

    def datetime_midnight(self, dt=None, utc=False):
        return self.utc_datetime_midnight(dt) if utc else self.local_datetime_midnight(dt)

    def seconds_since_midnight(self, dt=None, utc=False):
        return self.utc_seconds_since_midnight(dt) if utc else self.local_seconds_since_midnight(dt)

    # AWARE vs NAIVE

    # By design, these four functions don't perform any checks on their arguments.
    # The caller should ensure that they don't receive an invalid value like None.

    def is_aware(self, value):
        """
        Determines if a given datetime.datetime is aware.
        The logic is described in Python's docs:
        http://docs.python.org/library/datetime.html#datetime.tzinfo
        """
        return value.tzinfo is not None and value.tzinfo.utcoffset(value) is not None

    def is_naive(self, value):
        """
        Determines if a given datetime.datetime is naive.
        The logic is described in Python's docs:
        http://docs.python.org/library/datetime.html#datetime.tzinfo
        """
        return value.tzinfo is None or value.tzinfo.utcoffset(value) is None

    def make_aware(self, value, timezone=None):
        """
        Makes a naive datetime.datetime in a given time zone aware.
        """
        timezone = pytz.timezone(self.timezone(timezone))
        if hasattr(timezone, 'localize'):
            # This method is available for pytz time zones.
            return timezone.localize(value, is_dst=None)
        else:
            # Check that we won't overwrite the timezone of an aware datetime.
            if self.is_aware(value):
                raise ValueError('make_aware expects a naive datetime, got %s' % value)
            # This may be wrong around DST changes!
        return value.replace(tzinfo=timezone)

    def make_naive(self, value, timezone=None):
        """
        Makes an aware datetime.datetime naive in a given time zone.
        """
        timezone = pytz.timezone(self.timezone(timezone))
        # If `value` is naive, astimezone() will raise a ValueError,
        # so we don't need to perform a redundant check.
        value = value.astimezone(timezone)
        if hasattr(timezone, 'normalize'):
            # This method is available for pytz time zones.
            value = timezone.normalize(value)
        return value.replace(tzinfo=None)

    # OTHER

    def total_seconds(self, td):
        """Total seconds in the duration."""
        return ((td.days * 86400 + td.seconds) * 10 ** 6 + td.microseconds) / 10 ** 6


TimeConvert = TimeConvert()
