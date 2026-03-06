'''
Problem Description:
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

Approach:
-Use a loop to iterate upon the string
-Use a variable flag to detect if the first segment ends
-If another 1 is encountered, the loops stops and False is returned otherwise True is returned at the end

Time complexity: 
O(n): n is the size of the string

Space complexity:
O(1)
'''
class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = True
        for i in range(1,len(s)):
            if s[i] == "1" and flag == False:
                return False
            elif s[i] == "0" and flag == True:
                flag = False
        return True
