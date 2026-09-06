"""
Problem Description:
Given two strings s and t, return the number of distinct subsequences
of s that equal t.

Approach:
- Use recursion with two pointers:
    i -> current position in s
    j -> current position in t
- If t has been completely matched, return 1 because one valid
  subsequence has been formed.
- If s is exhausted before t is matched, return 0.
- When s[i] == t[j], there are two choices:
    1. Take s[i] and match it with t[j].
    2. Skip s[i] and try to match t[j] later.
- When s[i] != t[j], s[i] cannot be used to match t[j], so skip it.
- Memoize each (i, j) state to avoid solving the same subproblem
  multiple times.

Time Complexity:
O(m * n)

Reason:
- There are at most m * n distinct states, where
  m = len(s) and n = len(t).
- Each state performs O(1) work apart from recursive calls,
  which are memoized.

Space Complexity:
O(m * n)

Reason:
- The memo dictionary can contain O(m * n) states.
- The recursion stack can additionally reach O(m), which is
  dominated by O(m * n).
"""

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
            
        memo = {}

        def backtrack(i: int, j: int):
            
            # success 
            if  j>=len(t):
                return 1
            # exhaust all of s
            if i>=len(s):
                return 0

            # already checked
            if (i, j) in memo:
                return memo[(i, j)]

            # got the same character-> we can either take it or skip it

            if s[i] == t[j]:
                memo[(i, j )] = backtrack(i+1, j+1)+ backtrack(i+1, j)
            else:
                memo[(i, j)] = backtrack(i+1, j)
            

            return memo[(i, j)]
        
        return backtrack(0,0)
