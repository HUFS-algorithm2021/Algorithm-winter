#백준 1769번 yoongyo

x=input()
cnt=1
y=str(sum(int(element) for element in x))

while True:
    if len(str(y))==1:
        break
    cnt+=1
    y=str(sum(int(element) for element in y))

print(cnt if x!=y else 0)
print("YES" if int(y)%3==0 else "NO")


