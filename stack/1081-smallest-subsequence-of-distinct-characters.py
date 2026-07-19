"""
Problem Description:
Given a string s, return the lexicographically smallest
subsequence that contains every distinct character of s
exactly once.

Approach:
- Count the remaining occurrences of every character.
- Use a stack to build the answer greedily.
- For each character:
  - If it is already in the stack, skip it.
  - Otherwise, remove larger characters from the top of
    the stack if they appear again later.
  - Push the current character onto the stack.
- Join the stack to form the smallest subsequence.

Time Complexity:
O(n)

Reason:
- n = length of s.
- Each character is processed once.
- Every character is pushed and popped at most once.
- The stack contains at most 26 lowercase letters, so
  membership checks are O(1).

Space Complexity:
O(1)

Reason:
- The frequency map and stack each store at most the
  26 lowercase English letters.
"""

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        storage = {}

        for i in s:
            if i in storage:
                storage[i]+=1
            else:
                storage[i]=1
        
        stack =[]

        for i in s:
            if i not in stack:
                while stack and stack[-1]>i and storage[stack[-1]]>0:
                    stack.pop()
                
                stack.append(i)
            
            storage[i]-=1
        
        return "".join(stack)
