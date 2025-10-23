from datetime import datetime, time


def datetime_default():
    return datetime.combine(datetime.now(), time(15, 0))
