"""
Problem Description:
Given a collection of candidate numbers and a target, find all unique
combinations whose elements sum to target. Each candidate can be used
at most once, and duplicate combinations are not allowed.

Approach:
- Sort candidates to group duplicate values together.
- Use backtracking to explore including or excluding each candidate.
- When including a candidate, move to the next index so that each
  element is used at most once.
- Backtrack by removing the last added element after each recursive call.
- When excluding a candidate, skip its adjacent duplicates to avoid
  generating duplicate combinations.
- When target becomes zero, append a copy of the current combination.

Time Complexity:
O(2^n * n)

Reason:
- Each candidate has an include or exclude decision, producing up to
  O(2^n) subsets.
- Copying a valid combination can take up to O(n) time.
- Therefore, the worst-case time complexity is O(2^n * n), excluding
  the initial sorting cost of O(n log n).

Space Complexity:
O(n)

Reason:
- The recursion depth can reach O(n).
- The current combination stores at most n elements.
- Excluding the output list, auxiliary space is O(n).
"""
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        output = []
        candidates.sort()
        def backtrack(index: int, target: int, ans: list[int])->None:
            if target == 0:
                output.append(ans[:])
                return 

            if index>=len(candidates):
                return

            # include

            if candidates[index]<=target:
                ans.append(candidates[index])
                backtrack(index+1, target-candidates[index], ans)
                ans.pop()

                # exclude

            while index<len(candidates)-1 and candidates[index]== candidates[index+1]:
                index+=1
            backtrack(index+1, target, ans)


        backtrack(0, target, [])
        return output
