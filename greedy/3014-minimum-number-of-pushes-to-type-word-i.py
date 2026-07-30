"""
Problem Description:
Given a string of distinct lowercase letters, remap the
telephone keypad to minimize the total number of key
presses needed to type the string.

Approach:
- Since there are 8 keys (2–9), assign the first
  8 letters to require 1 push each.
- Assign the next 8 letters to require 2 pushes each,
  and so on.
- Traverse the string and accumulate the required pushes.

Time Complexity:
O(n)

Reason:
- The string is traversed exactly once.
- Each character contributes to the answer in O(1).

Space Complexity:
O(1)

Reason:
- Only a few variables are used.
"""

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        count = 2
        total = 0
        counter = 1
        for i in word:
            total +=counter
            count +=1
            if count > 9:
                count =2 
                counter+=1
        return total
