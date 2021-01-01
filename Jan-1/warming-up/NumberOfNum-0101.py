# 백준 2577 임나경

a = int(input())
b = int(input())
c = int(input())
num = a * b * c
num = str(num)
arr = [0] * 10
for i in range(len(num)):
    arr[int(num[i])] += 1
for i in range(10):
    print(arr[i])