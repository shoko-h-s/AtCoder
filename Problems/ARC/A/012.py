week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day = input()

if (day == "Saturday") or (day == "Sunday"):
    print(0)
else:
    # どの曜日の場合も、土曜日までの日数を求めればよい
    print(6 - week.index(day))
