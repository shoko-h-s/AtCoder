p_list = list(map(int, input().split()))

answer = ""

for p in p_list:
    answer += chr(p+96)
    
print(answer)
