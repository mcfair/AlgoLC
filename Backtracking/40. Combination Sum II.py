#coin change - use only once - backtracking
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        combo = []
        def dfs(target,k,bag):
            if target<0: return
            if target==0:
                bag= tuple(sorted(bag))
                combo.append(bag)
                return
            for i, c in enumerate(candidates[k:],k):
                dfs(target-c, i+1, bag+[c])
        
        dfs(target, 0, [])
        return list(set(combo))
                
