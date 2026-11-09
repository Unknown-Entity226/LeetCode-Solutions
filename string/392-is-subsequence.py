"""
Problem Description:
Given two strings s and t, determine whether s is a subsequence of t.
A subsequence is formed by deleting zero or more characters without
changing the relative order of the remaining characters.

Approach:
Use the two-pointer technique.

Maintain a pointer s_ptr to track the current character in s.

Traverse string t using t_ptr:
1. If all characters of s have been matched, return True.
2. If s[s_ptr] matches t[t_ptr], increment s_ptr.
3. Otherwise, continue traversing t without changing s_ptr.

After traversing t, return True if all characters of s have been matched;
otherwise, return False.

Time Complexity: O(n)
Reason: The algorithm traverses string t at most once, where n is len(t).

Space Complexity: O(1)
Reason: Only a constant number of pointer variables are used.
"""

class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_ptr = 0
        
        for t_ptr in range(len(t)):

            if s_ptr>=len(s):
                return True

            if s[s_ptr] == t[t_ptr]:
                s_ptr +=1

        if s_ptr>=len(s):
            return True

        return False
            
