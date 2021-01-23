#BOJ 10816 yoongyo

import sys
from collections import Counter #데이터의 개수를 셀 때 유용함. -> dic
'''Counter는 해시 가능한 객체를 세기 위한 dict 서브 클래스입니다. 
요소가 딕셔너리 키로 저장되고 개수가 딕셔너리값으로 저장되는 컬렉션입니다. 
개수가 0이나 음수를 포함하는 임의의 정수값이 될 수 있습니다.'''

n = sys.stdin.readline()
arr_n = Counter(sys.stdin.readline().strip().split(" "))

m = sys.stdin.readline()
arr_m = sys.stdin.readline().strip().split(" ")

for each in arr_m:
    print(arr_n[each], end=" ")