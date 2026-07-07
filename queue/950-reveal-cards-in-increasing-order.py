"""
Problem Description:
Given a deck of unique integers, arrange the cards so
that if we repeatedly:

1. Reveal the top card.
2. Move the next top card to the bottom.

the revealed sequence is in increasing order.

Return the required initial ordering.

Approach:
Instead of simulating the cards, simulate the positions.

- Sort the deck in increasing order.
- Store all indices (0 to n-1) in a queue.
- Repeatedly:
    - Remove the front index and place the next smallest
      card there.
    - If indices remain, move the next front index to
      the back of the queue.
- The resulting array represents the required ordering.

Time Complexity:
O(n log n)

Space Complexity:
O(n)
"""

class Solution(object):

    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        from collections import deque

        queue = deque()

        for i in range(len(deck)):
            queue.append(i)

        ans = [0] * len(deck)

        deck.sort()

        pointer = 0
        count = 0

        while queue:

            if count % 2 == 0:

                pos = queue.popleft()
                ans[pos] = deck[pointer]
                pointer += 1

            else:

                queue.append(queue.popleft())

            count += 1

        return ans
