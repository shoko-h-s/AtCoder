n = int(input())
r = input()

if r.count("F") == n:
    print(0)
    
else:
    score = 0
    
    score += r.count("A") * 4
    score += r.count("B") * 3
    score += r.count("C") * 2
    score += r.count("D")
    
    print(score / n)
