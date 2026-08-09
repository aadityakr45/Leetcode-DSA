1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        num_map=dict()
4        for i ,num in enumerate(nums):
5            diff=target-num
6            if diff in num_map:
7                return [num_map[diff],i]
8            num_map[num]=i