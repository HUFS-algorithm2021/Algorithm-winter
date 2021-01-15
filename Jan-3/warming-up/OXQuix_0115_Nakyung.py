# 백준 8958 임나경

num = int(input())
list = []
for i in range(num):
    tmp2 = input()
    list.append(tmp2)

count = [0] * num
tmp = 0
for i in range(num):
    for j in range(len(list[i])):
        if list[i][j] == 'O':
            tmp += 1
            count[i] += tmp
        else:
            tmp = 0
    tmp = 0
    print(count[i])
