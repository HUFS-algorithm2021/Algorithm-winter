# 백준 11726 2xn 타일링

n = int(input()) #크기 입력
DP = [1,1] #0일때도 1이라 생각하고 0,1 값을 넣음
for i in range(2,n+1): #2부터 n까지
    DP.append(DP[i-1]+DP[i-2]) #ㅣ를 하나 추가하거나 ㅡ 두개를 추가하거나
print(DP[-1]%10007) #구한 값을 10007로 나눈 나머지 출력