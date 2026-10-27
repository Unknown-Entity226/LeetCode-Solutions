"""
Problem Description:
Given two integers a and b, count the set bits in their binary
representations and calculate the score:
- If s1 >= s2, return s1 * s2.
- Otherwise, return s2 // s1.

Approach:
- Define a helper function to count set bits using Brian Kernighan's
  algorithm.
- Repeatedly clear the rightmost set bit using n &= (n - 1).
- Count the set bits of a and b separately.
- Apply the given conditions to calculate and return the score.
- s2//s1 works because a, b >= 1 (no division by zero error)

Time Complexity:
O(log a + log b)

Reason:
- Brian Kernighan's algorithm runs once for every set bit.
- Each integer has at most O(log n) bits, where n is the integer.
- Therefore, the total time is O(log a + log b) for positive inputs.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
- No additional data structure proportional to the input size is created.
"""
class Solution:
    def calculateScore(self, a: int, b: int) -> int:

        def count_set_bits(n):
            count = 0
            while n:
                n &= (n - 1)
                count += 1
            return count

        s1 = count_set_bits(a)
        s2 = count_set_bits(b)

        return s1*s2 if s1>=s2 else s2//s1
