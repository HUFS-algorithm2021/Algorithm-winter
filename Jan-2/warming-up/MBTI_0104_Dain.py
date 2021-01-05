# 20519 백준 강다인

def heart_distance(A, B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    return count


test = int(input())

for a in range(test):
    result = []
    person = int(input())
    mbti = list(input().split())

    for i in range(len(mbti)-2):
        count = 0
        j = i + 1
        temp = 0
        while count < 2:
            if j < len(mbti):
                temp += heart_distance(mbti[i], mbti[j])
                count += 1
                j += 1
            else:
                break
        if j < len(mbti)+1:
            temp += heart_distance(mbti[j-2], mbti[j-1])
        
        result.append(temp)

    result.sort()
    print(result[0])