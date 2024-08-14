from datetime import datetime, timedelta

def calculate_days_between_dates(date1_str, date2_str):
    """Вычисляет разницу в днях между двумя датами."""
    date1 = datetime.strptime(date1_str, "%Y-%m-%d").date()
    date2 = datetime.strptime(date2_str, "%Y-%m-%d").date()
    time_diff = date2 - date1
    return time_diff.days


date1 = "2022-01-01"
date2 = "2022-12-31"

print(f"Разница в днях: {calculate_days_between_dates(date1, date2)} дней")