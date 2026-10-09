1class Solution:
2    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        from collections import Counter
4        
5        # Count frequencies of elements in nums1
6        counts = Counter(nums1)
7        result = []
8        
9        # Iterate through nums2 to find matches
10        for num in nums2:
11            # If the number exists in our count map and has occurrences left
12            if num in counts and counts[num] > 0:
13                result.append(num)
14                counts[num] -= 1  # Decrement the count so we don't over-include it
15                
16        return result