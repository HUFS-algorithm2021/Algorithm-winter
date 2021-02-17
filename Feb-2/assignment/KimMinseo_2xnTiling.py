t = [0, 1, 3]
n = int(input())

for i in range(3, n+1):
  t.append((t[i - 2] * 2) + t[i - 1])

print(t[n] % 10007)