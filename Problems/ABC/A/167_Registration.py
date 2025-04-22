s = input()
t = input()

# s が t の接頭辞かどうか判定する
if t.startswith(s):
    print("Yes")
else:
    print("No")
