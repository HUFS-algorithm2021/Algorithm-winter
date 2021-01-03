#재귀_BOJ 10872
def fact(n):
    if(n==1):#이부분 생략했어서, n이 무한적으로 적어져서 오류남
        return 1
    return n * fact(n-1)#Big-0표기법에 의하면 실행시간은 O(n)

n = int(input())
answer = fact(n)
print(answer)