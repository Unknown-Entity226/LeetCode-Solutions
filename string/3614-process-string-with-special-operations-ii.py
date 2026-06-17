"""
Problem Description:
Build the final string using the operations:

    letter -> append
    *      -> delete last character
    #      -> duplicate string
    %      -> reverse string

Return the kth character of the final string.
If k is out of bounds, return '.'.

Approach:
Instead of constructing the final string:

1. Compute the final length.
2. Work backwards through the operations.
  if # operation:
   - half the current length 
   - if length becomes smaller than k then the chaaracter is in second half and we change k to k%length to get new k index in the first half
  if % operation:
   - make k = length - k - 1 (mirrored index)
  if * operation:
   - increase length by 1 
  if character :
   - decrease length by 1
   - if k becomes equal to length then we return the character
This avoids building potentially enormous strings.

Time Complexity:
O(N)

Space Complexity:
O(1)
"""
class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = 0
        for i in s:
            if i == "*":
                if length>0:
                    length-=1
            elif i == "#":
                length*=2
            elif i == "%":
                length = length
            else:
                length+=1
        if k>=length:
            return "."
        for i in range(len(s)-1, -1, -1):

            if s[i] == "#":
                length//=2
                if k >= length:
                    k = k%length
            elif s[i] == "%":
                k = length-k-1
            elif s[i] == "*":
                length +=1
            else:
                length -=1
                if k == length:
                    return s[i]
