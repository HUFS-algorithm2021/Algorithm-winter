#BOJ 1629 (분학정복) 이윤교

def power(a, b):
    if b == 1: # b의 값이 1이면
        return a % C #a % C return
    else:
        temp = power(a, b // 2)
        if b % 2 == 0: # b가 짝수인 경우
            return temp * temp % C
        else: # b가 홀수인 경우
            return temp * temp * a % C

A,B,C = map(int, input().split())
result = power(A,B)
print(result)