# BOJ 1074 z 탐색
import sys
input = sys.stdin.readline()

def z(n, r, c):
    global count
    if found == True: return
    if n == 2:
        temp = 0
        is_now(r, c)
        count += 1

        c += 1
        temp += 1
        is_now(r, c)
        count += 1

        r += 1
        c -= 1
        temp += 1
        is_now(r, c)
        count += 1

        c += 1
        temp += 1
        is_now(r, c)
        count += 1

        return
        
    else:
        z(n // 2, r, c)
        z(n // 2, r, c + n//2)
        z(n // 2, r + n//2, c)
        z(n // 2, r + n//2, c + n//2)

def is_now(r, c):
    if r == row and c == column:
        print(count)
        fount = True
        return True
    else:
        return False



N, row, column = map(int, input().split())
count = 0
found = False
z(pow(2, N), 0, 0)
# print(count)
