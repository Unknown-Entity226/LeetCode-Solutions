"""
Problem Description:
Given an array of distinct integers candidates and a target,
return all unique combinations whose sum equals the target.
Each candidate can be chosen unlimited times.

Approach:
- Use backtracking to explore all possible combinations.
- Iterate from the current index to avoid duplicate combinations.
- Choose the current candidate and recurse with the same index
  to allow unlimited reuse.
- Reduce the remaining target after each selection.
- If target becomes:
  - 0 → store the current combination.
  - Negative → stop exploring that path.
- Backtrack by removing the last chosen element.

Time Complexity:
O(N^(T/M))

- N = number of candidates.
- T = target.
- M = smallest candidate.


Space Complexity:
O(T/M)
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        output = []
        start = 0

        def recur(start, candidates, target, ans, output):

            if target == 0:
                output.append(ans[::])
                return 
            
            if target<0:
                return 
            
            for i in range(start, len(candidates)):
                if candidates[i]<=target:
                    ans.append(candidates[i])
                    recur(i, candidates, target-candidates[i], ans, output)
                    ans.pop()
        recur(start, candidates, target, ans, output)
        return output
