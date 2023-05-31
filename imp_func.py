import datetime
import typing
from birthdays_list import users, week


def get_birthdays_per_week(lst: typing.List[dict]) -> typing.List[dict]:
    b_list: typing.List[dict] = []
    one_week_int: typing.List[datetime] = [datetime.datetime.now().date() +
                                           datetime.timedelta(days=day) for day in
                                           range(1, 8)]
    for user in lst:
        if user['birthday'].month in [m.month for m in one_week_int] and \
                user['birthday'].day in [d.day for d in one_week_int]:
            w_day: int = datetime.datetime(year=datetime.datetime.now().year,
                                           month=user['birthday'].month,
                                           day=user['birthday'].day).weekday()
            w_day = 0 if w_day in range(5, 7) else w_day
            b_list.append({week[w_day]: user['name']})
    return b_list


for rec in get_birthdays_per_week(users):
    print(f'{list(rec.keys())[0]}: {", ".join(list(rec.values())[0])}')


# a little bit other implementation of this function
def get_birthdays(lst: typing.List[dict]) -> typing.List[dict]:
    current_date: datetime = datetime.datetime.now()
    bd_list: typing.List[dict] = []
    for user in lst:
        date_of_bd = datetime.datetime(year=current_date.year, month=user['birthday'].month, day=user['birthday'].day)
        if 0 <= (date_of_bd - current_date).days <= 7:
            bd_list.append({week[0]: user['name']}) if date_of_bd.weekday() in range(5, 7) else \
                bd_list.append({week[date_of_bd.weekday()]: user['name']})
    return bd_list


for rec in get_birthdays(users):
    print(f'{list(rec.keys())[0]}: {", ".join(list(rec.values())[0])}')
