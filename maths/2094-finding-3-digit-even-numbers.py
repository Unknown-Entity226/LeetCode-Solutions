"""
Problem Description:
Given an array of digits that may contain duplicates, generate all
unique three-digit even integers that can be formed by concatenating
three different elements from the array.

The generated number:
- Must have exactly three digits.
- Must not have a leading zero.
- Must be even.
- Each digit can only be used as many times as it appears in digits.

Approach:
- Build a frequency array of size 10 to store the number of occurrences
  of each digit.
- Choose the hundreds digit from 1 to 9 so that the number has no
  leading zero.
- Temporarily decrease its frequency.
- Choose the tens digit from 0 to 9.
- Temporarily decrease its frequency.
- Choose the units digit only from even digits (0, 2, 4, 6, 8).
- If the required digit is still available, construct the number.
- Restore frequencies after each choice so that the same digits can
  be reused in different numbers when available.
- Each combination of digit values is generated only once, so the
  result contains unique integers.

Time Complexity:
O(1)

Reason:
- There are only 10 possible digits.
- The algorithm examines at most 9 * 10 * 5 = 450 combinations.
- Therefore, with the fixed digit alphabet, the complexity is O(1).

Space Complexity:
O(1)

Reason:
- The frequency array contains exactly 10 elements.
- The result size is bounded by the number of possible three-digit
  even integers, so auxiliary space is O(1).
"""

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        

        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        result =[]

        for first in range(1, 10):
            if freq[first] == 0:
                continue

            freq[first] -= 1

            for second in range(10):
                if freq[second] == 0:
                    continue

                freq[second] -= 1

                for third in range(0, 10, 2):
                    if freq[third] > 0:
                        result.append(first*100+second*10+third)

                freq[second] += 1

            freq[first] += 1

        return result
