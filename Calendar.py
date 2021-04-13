import calendar
year, month, day = map(int, input().split())
days =  ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(days[(int(calendar.weekday(year, month, day)))])
