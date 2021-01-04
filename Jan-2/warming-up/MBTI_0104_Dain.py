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

    for i in range(person):
        temp = mbti[i]
        mbti[0], mbti[i] = mbti[i], mbti[0]
        for j in range(1, person):
            result.append(heart_distance(temp, mbti[j]))
        

    result.sort()

    print(result[0] + result[1] + result[2])

