#백준 1463번 yoongyo

n = int(input())
cnt = 0
dp = [0]*(n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    elif i%3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
print(dp[n])