word_set = {"and", "not", "that", "the", "you"}

n = int(input())
w_list = list(input().split())

w_set = set(w_list)

# w_set と word_set の積集合に要素があれば Yes
if w_set & word_set:
    print("Yes")
else:
    print("No")
