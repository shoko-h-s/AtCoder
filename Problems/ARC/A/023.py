import datetime

y = int(input())
m = int(input())
d = int(input())

ymd = datetime.date(y, m, d)
today = datetime.date(2014, 5, 17)

print((today - ymd).days)
