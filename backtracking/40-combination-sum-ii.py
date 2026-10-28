"""
Problem Description:
Given a collection of candidate numbers and a target, find all unique
combinations whose elements sum to target. Each candidate can be used
at most once, and duplicate combinations are not allowed.

Approach:
- Sort candidates to group duplicate values together.
- Use backtracking with include and exclude decisions for each candidate.
- Include the current candidate and recurse from the next index.
- Backtrack using pop() after exploring the include branch.
- Skip adjacent duplicate values in the exclude branch to avoid
  generating duplicate combinations.
- Stop exploring when the index reaches the end or the current
  candidate exceeds the remaining target.
- Store a copy of the combination whenever the target becomes zero.

Time Complexity:
O(n * 2^n)

Reason:
- Each candidate can be included or excluded, producing up to O(2^n)
  recursive possibilities.
- Copying a valid combination can take O(n) time.
- Sorting takes O(n log n), which is dominated by O(n * 2^n).

Space Complexity:
O(n) auxiliary space, excluding the output.

Reason:
- The recursion depth can reach O(n).
- The current combination can contain up to n elements.
- The output list may require exponential space in the worst case.
"""
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        output = []
        candidates.sort()
        def backtrack(index: int, target: int, ans: list[int])->None:
            if target == 0:
                output.append(ans[:])
                return 

            if index>=len(candidates) or candidates[index]>target:
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
