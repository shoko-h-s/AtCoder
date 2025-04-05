a, b = map(int, input().split())

if a == b:
    print("Draw")
elif a == 1:
    print("Alice")
elif b == 1:
    print("Bob")
    
else:
    if a > b:
        print("Alice")
    else:
        print("Bob")
