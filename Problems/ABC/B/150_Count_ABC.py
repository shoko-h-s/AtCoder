n = int(input())
s = input()

print(s.count("ABC"))



# 【別解】
# n = int(input())
# s = input()

# count = 0

# for i in range(n-2):
#     if s[i] == "A":
#         if (s[i+1] == "B") and (s[i+2] == "C"):
#             count += 1
            
# print(count)
