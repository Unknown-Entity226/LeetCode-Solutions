"""
Problem Description:
Given an integer array, return the maximum possible
product of any three numbers.

Approach:
- Maintain the three largest numbers.
- Maintain the two smallest numbers.
- The answer is the maximum of:
  - Product of the three largest numbers.
  - Product of the two smallest numbers and the
    largest number.

Time Complexity:
O(n)

Reason:
- The array is traversed once.
- Each element updates at most five variables.

Space Complexity:
O(1)

Reason:
- Only five variables are used regardless of input size.
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,s,t = -1001, -1001, -1001
        
        a, b = 1001, 1001
        
        for i in nums:
            if i<=a:
                b = a
                a = i
            elif i<b: 
                b = i
                
            if i>=l:
                t = s
                s = l
                l = i
            elif i>=s:
                t = s
                s = i
            elif i>t:
                t = i
                
        return max(a*b*l, l*s*t)
