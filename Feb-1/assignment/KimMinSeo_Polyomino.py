#1343 BOJ 김민서
poly = input()
poly =poly.replace("XXXX","AAAA")
poly = poly.replace("XX","BB")

if 'X' in poly:
    print(-1)
else:
    print(poly)