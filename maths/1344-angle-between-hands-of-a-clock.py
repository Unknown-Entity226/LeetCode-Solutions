"""
Problem Description:
Given an hour and minutes, return the smaller angle
between the hour hand and the minute hand of a clock.

Approach:
- The hour hand moves:
      360 / 12 = 30 degrees per hour
  and also moves continuously as minutes pass:

      0.5 degrees per minute

- The minute hand moves:

      360 / 60 = 6 degrees per minute

- Compute the positions of both hands.
- Take the absolute difference.
- Return the smaller of:
      angle
      360 - angle

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

class Solution(object):

    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """

        if hour == 12:
            hour = 0

        hourhand = hour * 30 + 0.5 * minutes
        minutehand = 6 * minutes

        angle = abs(hourhand - minutehand)

        return angle if angle <= 180 else 360 - angle
