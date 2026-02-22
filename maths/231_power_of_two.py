'''
Problem Description:
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Approach:
-Create an int_max variable (maximum value allowed as per constraints) having value 2**31
-Check the remainder of divinding int_max with n(given integer).
-If remaineder is 0, return True otherwise False.
-An additional check case is inserted to check if the n is 0 or negative and returns False in this case. 

Time Complexity:
O(1)

Space Complexity:
O(1)
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
            
        int_max = 2**31

        if int_max%n==0:
            return True
        return False
