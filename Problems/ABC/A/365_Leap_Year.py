y = int(input())

if y % 4 != 0:
    print(365)
elif (y % 4 == 0) and (y % 100 != 0):
    print(366)
elif (y % 100 == 0) and (y % 400 != 0):
    print(365)
elif y % 400 == 0:
    print(366)


'''
【別解】calendarモジュールを使う場合

import calendar

y = int(input())

if calendar.isleap(y):
    print(366)
else:
    print(365)
'''
