# 백준 9935 강다인

Ex = input()
c4 = input()

while True:
    index = Ex.find(c4)
    if index != -1:
        Ex = Ex[0:index] + Ex[index + len(c4):]
    else:
        break

if Ex == "":
    print("FRULA")
else:
    print(Ex)