abcd = input()

a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

if a + b + c + d == 7:
    op_list = ["+", "+", "+"]
elif a - b + c + d == 7:
    op_list = ["-", "+", "+"]
elif a + b - c + d == 7:
    op_list = ["+", "-", "+"]
elif a + b + c - d == 7:
    op_list = ["+", "+", "-"]
elif a + b - c - d == 7:
    op_list = ["+", "-", "-"]
elif a - b + c - d == 7:
    op_list = ["-", "+", "-"]
elif a - b - c + d == 7:
    op_list = ["-", "-", "+"]
else:
    op_list = ["-", "-", "-"]

print(f"{a}{op_list[0]}{b}{op_list[1]}{c}{op_list[2]}{d}=7")
