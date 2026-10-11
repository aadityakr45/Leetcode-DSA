1class Solution:
2    def buildArray(self, target: list[int], n: int) -> list[str]:
3        results = []
4        target_set = set(target)
5        max_val = target[-1]  # We only need to process up to the last element in target
6        
7        for i in range(1, max_val + 1):
8            results.append(Push)
9            if i not in target_set:
10                results.append(Pop)
11                
12        return results