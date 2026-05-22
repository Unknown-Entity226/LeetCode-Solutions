'''
Problem Description:
A number is picked between 1 and n.

You must guess the number using the API:

    guess(num)

Returns:
    -1 → num is too high
     1 → num is too low
     0 → correct guess

Return the picked number.

Approach:
- Use Binary Search on range [1, n].
- At each step:
    - Guess the middle number.
    - If guess is too high:
          search left half
    - If guess is too low:
          search right half
    - If correct:
          return the number

- Since the search space halves each iteration,
  binary search is optimal.

Time Complexity:
O(log n)

Space Complexity:
O(1)
'''
# The guess API is already defined for you.
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        low = 1
        high = n

        while low <= high:

            mid = (low + high) // 2
            result = guess(mid)

            if result == -1:
                high = mid - 1

            elif result == 0:
                return mid

            else:
                low = mid + 1
