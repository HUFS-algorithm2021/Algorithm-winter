#BOJ 1010번 다리놓기 leeyoongyo

import math

T = int(input()) #테스트 케이스의 개수 T
for i in range (T):
    n,m = map(int,input().split()) #강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)
    #조합 nCr = n! / (r! * (n-r)!)
    m_fact = math.factorial(m)
    n_fact = math.factorial(n)
    mn_fact = math.factorial(m-n)
    print(m_fact // (n_fact * mn_fact))
