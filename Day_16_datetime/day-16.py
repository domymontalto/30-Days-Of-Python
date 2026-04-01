from datetime import datetime, date

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year
current_hour = datetime.now().hour
current_minute = datetime.now().minute
print(f'Current time {current_month}/{current_day}/{current_year}, {current_hour}:{current_minute}')

print()

print(datetime.now().timestamp())

print()

now = datetime.now()
current_day = now.strftime('%m/%d/%Y, %H:%M:%S')
print(current_day)

print()

today = 'December 5 2019'
time_today = datetime.strptime(today, '%B %d %Y')
print(time_today)

print()

now = date(month = 3, day = 31, year = 2026)

new_year = date(month = 12, day = 31, year = 2026)

print(new_year - now)

print()

date_1970 = date(month = 1, day = 1, year = 1970)
print(now - date_1970)

print()

# I can use the datetime module to display the date of the top workout within the app