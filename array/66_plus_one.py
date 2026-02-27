'''
Problem Description:
You are given a large integer represented as an array of digits,
where digits[i] is the i-th digit of the integer.
The digits are stored in left-to-right order (most significant to least significant).
The integer does not contain leading zeros.

Increment the integer by one and return the resulting array of digits.

Approach:
- Start from the least significant digit (rightmost).
- Add 1 (carry = 1 initially).
- For each digit:
    - Compute total = current digit + carry.
    - Update digit as total % 10.
    - Update carry as total // 10.
- Continue propagating carry toward the left.
- If carry remains after processing all digits:
    - Insert it at the beginning of the array.

Note:
- The shifting logic below manually moves elements right to
  insert the final carry at index 0.

Time Complexity:
O(n), where n is the number of digits.

Space Complexity:
O(1) extra space (in-place modification, ignoring final carry expansion).
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            carry = total // 10
            digits[i] = total % 10

        if carry != 0:
            idx = 0
            digits.append(digits[-1])
            temp = digits[idx]

            while idx < len(digits) - 1:
                cur = digits[idx + 1]
                digits[idx + 1] = temp
                temp = cur
                idx += 1

            digits[0] = carry

        return digits
