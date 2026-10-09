1class Solution:
2    def sortedSquares(self, nums: list[int]) -> list[int]:
3        l=0
4        r=len(nums)-1
5        p=r
6        cont=[0]*len(nums)
7        while l<=r:
8            if abs(nums[l])>abs(nums[r]):
9                n=nums[l]*nums[l]
10                l=l+1
11            else:
12                n=nums[r]*nums[r]
13                r=r-1
14            cont[p]=n
15            p=p-1
16        return cont