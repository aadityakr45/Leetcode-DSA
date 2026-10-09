1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        d=dict()
4        for i in s:
5            if i in d:
6                d[i]=d[i]+1
7            else:
8                d[i]=1
9        for i in d:
10            if d[i]==1:
11                return s.index(i)
12        return -1