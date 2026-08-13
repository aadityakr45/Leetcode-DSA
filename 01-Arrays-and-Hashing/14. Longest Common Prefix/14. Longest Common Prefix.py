1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        lg_cm_str=
4        strs.sort()
5        first_ele=strs[0]
6        last_ele=strs[-1]
7        for i in range(min(len(first_ele),len(last_ele))):
8            if first_ele[i]!=last_ele[i]:
9                return lg_cm_str
10            lg_cm_str+=first_ele[i]
11        return lg_cm_str
12
13
14        