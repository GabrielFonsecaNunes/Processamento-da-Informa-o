v = []

for i in range(2):
    v.append(int(input()))

print(1 if v[0] ^ v[1] else 0)