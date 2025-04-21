n = int(input())
c = input()

c_count = [c.count("1"), c.count("2"), c.count("3"), c.count("4")]

print(max(c_count), min(c_count))
