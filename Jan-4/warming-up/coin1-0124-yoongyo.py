#BOJ 2293 yoongyo

import sys
n,k = map(int,sys.stdin.readline().split()) #n가지 종류의 동전과 가치의 합 k
value = [int(sys.stdin.readline()) for i in range(n)] #각각의 동전의 가치

dp = [0] * (k+1)
dp[0] = 1 #해당 동전을 한개만 썼을때 값을 추가하기위함

for i in value: #각각의 코인의 종류 전부 순회
    for j in range(i,k+1): # 이전에 만들수 있었던 가치에 있던 배열의 값을 받아와 해당 코인의 가치를 더해 배열에 넣어줌.
        if j-i >= 0 :
            dp[j] += dp[j-i]
print(dp[k])


