"""
Problem Description:
Given a string s and a positive integer k, find the maximum number of
non-overlapping palindromic substrings whose lengths are at least k.

Approach:
- Scan the string from left to right.
- For each starting position, first check whether the substring of
  length k is a palindrome.
- If it is not, check the substring of length k+1.
- If either is a palindrome, select it and continue after the selected
  substring.
- Otherwise, move the starting position forward by one.
- The greedy strategy selects the earliest possible palindrome, leaving
  the maximum possible remaining portion of the string for future
  substrings.

Time Complexity:
O(n^2)

Reason:
- There are O(n) iterations of the main scan.
- Each palindrome check can take O(n) in the worst case.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
- isPal() uses constant auxiliary space.
"""

class Solution:

    def isPal(self, arr, start, end):

        while start<end:
            if arr[start]!=arr[end]:
                return False
            start+=1
            end-=1
        return True
    def maxPalindromes(self, s: str, k: int) -> int:
        start = 0
        end = k-1
        count = 0
        while end<len(s):
            if self.isPal(s, start, end):
                start =end +1
                end+=k
                count+=1

            elif self.isPal(s, start, min(end+1, len(s)-1)):
                start = end+2
                end+=k+1
                count+=1

            else:
                start+=1
                end+=1
        return count

                    
