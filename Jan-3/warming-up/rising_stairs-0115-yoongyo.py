#BOJ 2579 이윤교

n = int(input()) #rPeksdml rotn
stairs = [0 for i in range(301)] #계단의 개수는 300이하의 자연수
dp = [0 for i in range(301)] #계단의 개수만큼 dp 생

for i in range(n):
    stairs[i] = int(input()) #각 계단에 쓰여 있는 점수 입력받기

dp[0] = stairs[0] #base
dp[1] = stairs[0] + stairs[1] #base
dp[2] = max(stairs[0]+stairs[2] , stairs[1]+stairs[2]) #base

for i in range(3,n):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i - 2] + stairs[i] ) #dp
print(dp[n - 1]) #얻을 수 있는 총 점수