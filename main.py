from datetime import datetime, date

def days_until_new_year():
    today = date.today()
    new_year = date(today.year + 1, 1, 1)
    days_left = (new_year - today).days
    return days_left

print(f"До Нового года осталось: {days_until_new_year()} дней!")