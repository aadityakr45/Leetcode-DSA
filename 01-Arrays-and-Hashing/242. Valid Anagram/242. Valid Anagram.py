1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        from collections import Counter 
4        if len(s)!=len(t):
5            return False
6        count=Counter(s)
7        for char in t:
8            if char not in count:
9                return False
10            else:
11                count[char]=count[char]-1
12                if count[char]<0:
13                    return False
14        return True 