n = int(input())
s_list = input().split()

# Y が含まれているかどうかのみで場合分け可能
if "Y" in s_list:
    print("Four")
else:
    print("Three")
