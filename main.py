import numpy as np
import datetime


def onDay(date, day):
    days = (day - date.weekday() + 7) % 7
    return date + datetime.timedelta(days=days)


def weeks(_data, _n):
    t = [onDay(_data, 0)]
    for i in range(0, _n - 1):
        t.append(onDay(t[-1], 6))
        t.append(onDay(t[-1], 0))
    t.append(onDay(t[-1], 6))
    t = np.array(t).reshape(_n, 2)
    return t
