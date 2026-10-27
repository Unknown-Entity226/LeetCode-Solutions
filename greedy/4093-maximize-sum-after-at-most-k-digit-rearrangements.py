"""
Problem Description:
Given an integer array nums and an integer k, maximize the sum
of the array by rearranging the decimal digits of at most k
elements. Each operation rearranges the digits of one element
to form a new integer.

Approach:
- Define rearrange(num) to extract the digits of a number.
- Sort the digits and rebuild the largest possible integer.
- Calculate the gain from rearranging each element.
- Sort the gains in descending order.
- Add the largest k gains to the original sum.

Time Complexity:
O(n log n + d log d)

Reason:
- Rearranging each number takes O(d log d), where d is its
  maximum number of decimal digits.
- Computing all gains takes O(n * d log d).
- Sorting the n gains takes O(n log n).
- Selecting the largest k gains takes O(k) for slicing and summing.
- Overall, the time complexity is O(n * d log d + n log n).
  If d is bounded, this simplifies to O(n log n).

Space Complexity:
O(n + d)

Reason:
- The gains list stores n elements, requiring O(n) space.
- The digit list requires O(d) space for one number.
- Therefore, auxiliary space is O(n + d).
"""
class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:

        def rearrange(num: int)->int:
            digits = []

            while num:
                digits.append(num%10)
                num//=10

            digits.sort()

            num = 0
            for i in range(len(digits)-1, -1, -1):
                num = num*10+digits[i]

            return num

        gains = []

        for num in nums:
            gains.append(rearrange(num) - num)

        gains.sort(reverse=True)

        return sum(nums) + sum(gains[:k])
