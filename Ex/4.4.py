def gen_secs():
    secs = 0
    while secs < 60:
        yield secs
        secs += 1
def gen_minutes():
    mins = 0
    while mins < 60:
        yield mins
        mins += 1
def gen_hours():
    hours = 0
    while hours < 24:
        yield hours
        hours += 1
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)
def gen_years(start=2025):
    while True:
        yield start
        start += 1
def gen_months():
    months = 1
    while months <= 12:
        yield months
        months += 1

def gen_days(amount_days, leap_year=False):
    days = 1
    while days <= amount_days:
        if leap_year and days == 29:
            yield 29
            days += 1
            continue
        yield days
        days += 1
def gen_date():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            if month in [1, 3, 5, 7, 8, 10, 12]:
                days_in_month = 31
            elif month in [4, 6, 9, 11]:
                days_in_month = 30
            else:  # February
                days_in_month = 29 if leap_year else 28
            for day in gen_days(days_in_month, leap_year):
                yield "%04d-%02d-%02d" % (year, month, day)

def main():
    for date in gen_date():
        for time in gen_time():
            print(f"{date} {time}")

if __name__ == "__main__":
    main()