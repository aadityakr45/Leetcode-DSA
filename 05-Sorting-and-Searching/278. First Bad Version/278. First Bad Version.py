1class Solution(object):
2    def firstBadVersion(self, n):
3        left, right = 1, n
4        while left < right:
5            mid = (left + right) // 2
6            if isBadVersion(mid):
7                right = mid
8            else:
9                left = mid + 1
10        return left