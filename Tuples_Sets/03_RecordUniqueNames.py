# [print(name) for name in {input() for _ in range(int(input()))}]

n = int(input())
names = []
for _ in range(n):
    names.append(input())
unique = set(names)
for n in unique:
    print(n)
