1class Solution:
2    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
3        '''results=[]
4        for i in range(1,len(nums)+1):
5            if i not in nums:
6                results.append(i)
7        return results'''
8
9        from collections import Counter
10        freq=Counter(nums)
11        results=[]
12        for i in range(1,len(nums)+1):
13            if i not in freq.keys():
14                results.append(i)
15        return results