1class Solution:
2    def findMaxAverage(self, nums: list[int], k: int) -> float:
3        curr_sum=sum((nums[:k]))
4        max_sum=curr_sum
5        for i in range(k,len(nums)):
6            curr_sum=curr_sum-nums[i-k]+nums[i]
7            max_sum=max(max_sum,curr_sum)
8        return max_sum/k