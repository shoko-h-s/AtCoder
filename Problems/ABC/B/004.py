list_c0 = list(input().split())
list_c1 = list(input().split())
list_c2 = list(input().split())
list_c3 = list(input().split())

list_c0_r = list_c0[::-1]
list_c1_r = list_c1[::-1]
list_c2_r = list_c2[::-1]
list_c3_r = list_c3[::-1]

print(*list_c3_r)
print(*list_c2_r)
print(*list_c1_r)
print(*list_c0_r)
