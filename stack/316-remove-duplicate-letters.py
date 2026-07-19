"""
Problem Description:
Given a string s, remove duplicate letters so that every
letter appears exactly once. Among all possible results,
return the lexicographically smallest one.

Approach:
- Count the remaining occurrences of every character.
- Use a stack to build the answer.
- For each character:
  - If it is already in the stack, skip it.
  - Otherwise, remove larger characters from the top of
    the stack if they appear again later.
  - Push the current character onto the stack.
- Join the stack to obtain the final string.

Time Complexity:
O(n)

Reason:
- n = length of s.
- Each character is processed once.
- Every character is pushed onto the stack at most once
  and popped at most once.
- Dictionary operations are O(1) on average.

Space Complexity:
O(1)

Reason:
- The no. of distinct characters to be stored is at max 26, so O(26) = O(1)
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
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
