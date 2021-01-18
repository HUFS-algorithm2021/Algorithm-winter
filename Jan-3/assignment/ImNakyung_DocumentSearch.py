# 백준 1543 임나경

doc = input()
word = input()
count = 0
tmp = ''
for i in doc:
    tmp += i
    if tmp.find(word) != -1:
        count += 1
        tmp = ''
    else: pass
print(count)