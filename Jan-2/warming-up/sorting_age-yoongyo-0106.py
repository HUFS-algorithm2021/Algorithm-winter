#백준 10814번 yoongyo

n = int(input())
list = []

for i in range(n):
    age, name = map(str,input().split())
    list.append((int(age),name))
list.sort(key=lambda list:list[0])

for s in list:
    print(s[0],s[1])
