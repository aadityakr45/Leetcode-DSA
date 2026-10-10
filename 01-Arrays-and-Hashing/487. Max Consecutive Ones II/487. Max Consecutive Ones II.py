1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        count,max_count=0,0
4        for i in range(len(nums)):
5            if nums[i]==1:
6                count=count+1
7            else:
8                max_count=max(count,max_count)
9                count=0
10        return max(count,max_count)
11
12        