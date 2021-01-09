#백준 1929번 yoongyo
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
m,n = map(int,input().split())
for i in range(m,n+1):
    if(is_prime(i)):
        print(i)
