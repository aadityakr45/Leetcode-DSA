1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        max_sub=float('-inf')
4        curr_max=0
5        for i in nums:
6            curr_max=max(i,curr_max+i)
7            max_sub=max(max_sub,curr_max)
8        return max_sub
9              
10        