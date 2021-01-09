# 백준 9935 강다인

Ex = input()
c4 = input()

while True:
    if c4 in Ex:
        Ex = Ex.replace(c4, "")
    else:
        break

if Ex == "":
    print("FRULA")
else:
    print(Ex)