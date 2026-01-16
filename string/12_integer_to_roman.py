'''
Problem Description:
Given an integer, convert it to a Roman numeral.
Approach (Greedy)
->Define a mapping of integer values to their Roman numeral symbols, including subtractive cases.
->Process the values in descending order.
->For each value:
->While the number is greater than or equal to the current value, append the corresponding Roman symbol.
->Subtract the value from the number.
->Continue until the number becomes zero.
->This greedy approach ensures the largest possible Roman numeral is used at each step.
Time complexity: O(1) - The number of Roman numeral symbols is fixed.
'''
#Python Implementation
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d= {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        result = ""
        for key in sorted(d.keys(), reverse=True):
            while num>=key:
                result += d[key]
                num-=key
        return result