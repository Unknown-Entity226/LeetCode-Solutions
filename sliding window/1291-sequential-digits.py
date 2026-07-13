"""
Problem Description:
Return all integers in the range [low, high] whose digits
are sequential, i.e., every digit is exactly one greater
than the previous digit.

Approach:
- Store "123456789" as the source string.
- Compute the number of digits in low and high.
- For every possible digit length:
  - Generate sequential numbers using a sliding window.
  - Update the current number efficiently instead of
    rebuilding it from scratch.
  - Add the number if it lies within the given range.
- Return the generated numbers.

Time Complexity:
O(1)

Reason:
- At most 9 digit lengths are possible.
- For each length, at most 9 sequential numbers are generated.
- The total number of generated candidates is bounded by a
  small constant (36), independent of the input values.

Space Complexity:
O(1)

Reason:
- Uses only a few variables.
- Excluding the output list.
"""

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        nums = "123456789"

        lenOfLow = 0
        lenOfHigh = 0
        temp =  low
        while temp:
            temp//=10
            lenOfLow+=1

        temp = high
        while temp:
            temp//=10
            lenOfHigh+=1
        ans = []
        mod = 10**(lenOfLow-1)
        for i in range(lenOfLow, lenOfHigh+1):
            left = 0
            right = i
            n = int(nums[left:right])

            while right<=len(nums):
                if right>i:
                    n = n*10+int(nums[right-1])
                if n>=low and n<=high:
                    ans.append(n)
                right +=1
                left+=1
                n%=mod
            mod*=10
        return ans
