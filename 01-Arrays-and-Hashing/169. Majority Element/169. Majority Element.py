1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        d=dict()
4        for i in nums:
5            if i in d:
6                d[i]=d[i]+1
7            else:
8                d[i]=1
9        for i in d:
10            if d[i]>(len(nums)//2):
11                return i