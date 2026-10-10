1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        i=0
4        j=n
5        temp=list()
6        while i<n:
7            temp.append(nums[i])
8            temp.append(nums[j])
9            i=i+1
10            j=j+1
11        return temp
12