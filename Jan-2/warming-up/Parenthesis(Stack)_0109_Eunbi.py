# 백준 9012 김은비

def parChecker(parSeq):
	S = []
	for i in parSeq:
		if i == '(': 
			S.append(i)
		else: # i == ')'
			if not S: #원소가 없으면  Parenthesis가 아님
				print("NO")
				return
			else: 
				S.pop()
	if not S: #남아있는 원소가 없으면  Parenthesis가 맞음
		print("YES")
		return
	else: #아니면 Parenthesis가 아님
		print("NO")
		return

n = int(input())
for i in range(n):
	parSeq = input()
	parChecker(parSeq)
