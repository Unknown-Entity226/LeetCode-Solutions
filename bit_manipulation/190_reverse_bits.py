'''
Problem Description:
Reverse the bits of a given 32-bit unsigned integer and return the result.

The input is treated as a 32-bit integer.
The output should also be a 32-bit integer with bits reversed.

Approach (As Implemented Below):
- Initialize a variable `result` to store the reversed bits.
- Maintain a `power` variable starting from 31 (most significant bit position).
- Extract bits from the input number one by one using modulo (n % 2).
- Shift each extracted bit to its reversed position using left shift (<<).
- Reduce the number using integer division (n // 2).
- Continue until n becomes 1, then place the final bit manually.

Note:
- This approach works by reconstructing the reversed bit pattern.
- The loop stops when n becomes 1 and handles the last bit separately.

Time Complexity:
O(32) → constant time, since the integer has 32 bits.

Space Complexity:
O(1)
'''
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n

        result = 0
        power = 31

        while n != 1:
            result += (n % 2) << power
            power -= 1
            n = n // 2

        result += 1 << power
        return result
