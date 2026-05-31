"""
Problem Description:
You are given the initial mass of a planet and an array of asteroid masses.

The planet can collide with asteroids in any order.

Rules:
- If planet_mass >= asteroid_mass:
      the asteroid is destroyed
      the planet gains asteroid_mass
- Otherwise:
      the planet is destroyed

Return True if all asteroids can be destroyed, otherwise return False.

Approach:
- To maximize the planet's chances of survival, destroy the smallest
  asteroids first.
- Sort the asteroid masses in ascending order.
- Iterate through the sorted array:
    - If the current asteroid is larger than the planet's mass,
      return False.
    - Otherwise, absorb the asteroid and increase the planet's mass.
- If all asteroids are processed successfully, return True.

Time Complexity:
O(n log n)
- Sorting dominates the runtime.

Space Complexity:
O(1)
- Ignoring the space used by the sorting algorithm.
"""

class Solution(object):

    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """

        asteroids.sort()

        for i in range(len(asteroids)):

            if asteroids[i] > mass:
                return False

            mass += asteroids[i]

        return True
