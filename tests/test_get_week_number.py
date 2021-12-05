import datetime
from datetime import date

from run import get_week_number

AMOUNT_WEEKS = 5000


def test_oldest_dates():
    """ Тест дат до начала первой недели
    """
    assert get_week_number(date(1, 1, 1)) == 1
    assert get_week_number(date(2018, 12, 29)) == 1


def test_first_week():
    for i in range(7):
        assert get_week_number(date(2018, 12, 30) + datetime.timedelta(days=i)) == 1


def test_second_week():
    for i in range(7):
        assert get_week_number(date(2018, 12, 30) + datetime.timedelta(days=7 + i)) == 2


def test_every_week(amount=AMOUNT_WEEKS):
    """ Тест {amount} недель после начальной даты
    """
    for week_num in range(1, amount + 1):
        ith_week(week_num)


def ith_week(week_num):
    """ Тест {week_num} недели по счету
    """
    for i in range(7):
        assert get_week_number(date(2018, 12, 30) + datetime.timedelta(days=(week_num - 1) * 7 + i)) == week_num
