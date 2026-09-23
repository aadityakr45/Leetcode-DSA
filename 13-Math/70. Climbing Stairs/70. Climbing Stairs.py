1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n<=2:
4            return n
5        dp=[0]*(n+1)
6        dp[1]=1
7        dp[2]=2
8        for i in range(3,n+1):
9            dp[i]=dp[i-1]+dp[i-2]
10        return dp[n]
11        