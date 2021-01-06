N = int(input())
num_list = list(map(int, input().split()))
num = []
for i in range(N):
    temp = []
    numTo = str(num_list[i])
    for j in numTo:
        temp.append(int(j))
    temp.append(int(num_list[i]))
    num.append(temp)

# num.sort(reverse=True)
# # num.sort()

for n in range(len(num) - 1):
    for i in range(max(len(num[n]), len(num[n+1])) - 1):
        if num[n][i] >= 10:
            if num[n+1][i] > 0 and num[n+1][i] < 10:
                num[n], num[n + 1] = num[n + 1], num[n]
            else:
                break
        elif num[n+1][i] >= 10:
            if num[n][i] > 0 and num[n][i] < 10:
                num[n], num[n + 1] = num[n + 1], num[n]
            else:
                break
        else:
            if num[n][i] > num[n+1][i]:
                num[n], num[n+1] = num[n+1], num[n]

# print(num)
s = ""
for j in num:
    s += str(j[-1])
print(int(s))