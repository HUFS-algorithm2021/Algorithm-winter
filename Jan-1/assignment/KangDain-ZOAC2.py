alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lpha = [ 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25]
zoac = input()  # DAIN
pointer = 0
counter = 0
for i in zoac:
    index = alpha.index(i) # 탐색할 값의 인덱스
    forward = 0 # 정방향 탐색 가중치
    reverse = 0 # 역방향 탐색 가중치
    # 정방향 탐색
    if index < pointer:
        forward = 26 - (pointer - index)
    else:
        forward = index - pointer
    
    if index > pointer:
        reverse = 26 - (index - pointer)
    else:
        reverse = pointer - index

    counter += forward if forward <= reverse else reverse
    pointer = index

print(counter)
