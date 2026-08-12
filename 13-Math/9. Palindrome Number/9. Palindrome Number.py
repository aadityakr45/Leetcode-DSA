1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3       
4        if x<0:
5            return False
6        else:
7            n=x
8            sum=0
9            while x>0:
10                r=x%10
11                sum=sum*10+r
12                x=x//10
13            return sum==n
14
15        