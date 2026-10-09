1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left=0
4        right=len(s)-1
5        while left<right:
6            while left<right and not s[left].isalnum():
7                left=left+1
8            while left<right and not s[right].isalnum():
9                right=right-1
10            if s[left].lower() != s[right].lower():
11                return False
12            left=left+1
13            right=right-1
14        return True