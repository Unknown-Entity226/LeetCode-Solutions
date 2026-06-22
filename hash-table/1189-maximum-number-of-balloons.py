"""
Problem Description:
Given a string text, determine the maximum number of times
the word "balloon" can be formed using the characters in text.

Each character can be used at most once.

Approach:
- Count the occurrences of:
      b, a, l, o, n
- The word "balloon" requires:
      b -> 1
      a -> 1
      l -> 2
      o -> 2
      n -> 1
- The answer is the minimum available count among the
  required characters after accounting for multiplicity.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        store = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for i in text:

            if i == "a" or i == "b" or i == "l" or i == "n" or i == "o":
                store[i] += 1

        count = store["a"]

        for i in store:

            if i == "a" or i == "b" or i == "n":
                count = min(count, store[i])

            else:
                count = min(count, store[i] // 2)

        return count
