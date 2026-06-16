"""
Problem Description:
There are n bulbs, all initially off.

Round 1:
    Toggle every bulb.

Round 2:
    Toggle every 2nd bulb.

Round 3:
    Toggle every 3rd bulb.

...

Round n:
    Toggle only the nth bulb.

Return the number of bulbs that remain on after all rounds.

Approach:
- A bulb is toggled once for every divisor of its position.
- Most numbers have divisors in pairs:

      (1, n)
      (2, n/2)
      ...

  so they are toggled an even number of times and end up off.

- Only perfect squares have an odd number of divisors.

- Therefore, the bulbs that remain on are exactly those at
  positions:

      1, 4, 9, 16, ...

- The number of perfect squares ≤ n is:

      floor(sqrt(n))

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

class Solution(object):

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int(n ** 0.5)
