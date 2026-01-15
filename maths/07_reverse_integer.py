'''
Problem description:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Approach:
->Initialize ans to 0 to store the reversed number.
->Extract the last digit of x using modulo (x % 10).
->Before appending the digit, check whether multiplying ans by 10 would cause an overflow.
->If overflow is detected, return 0.
->Append the digit and reduce x by dividing it by 10.
->Continue until all digits are processed.
Time Complexity: O(d), where d is the number of digits in x
'''
#Python Implemention
class Solution(object):
    def reverse(self, x):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        ans = 0
        while x != 0:
            digit = x % 10 if x > 0 else -(abs(x) % 10)
            x //= 10
            if ans < INT_MIN // 10 or ans > INT_MAX // 10:
                return 0
            ans = ans * 10 + digit
        return ans
