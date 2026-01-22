a = int(input())
b = list(input())

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * ((int(b[0]) * 100) + ((int(b[1]) * 10)) + (int(b[2]))))