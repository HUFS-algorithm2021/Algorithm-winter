#BOJ 11279 yoongyo
import heapq #최소힙 지원
import sys

numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num)) #음수로 만들어 push
    else:
        try:
            print(-1 * heapq.heappop(heap))#-1을 곱하면서 출력 (음수 -> 양수)
        except:
            print(0)