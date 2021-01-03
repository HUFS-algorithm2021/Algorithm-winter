# 백준 2750 임나경

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
[print(nums[_]) for _ in range(n)]