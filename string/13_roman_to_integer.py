'''Problem Description
Given a Roman numeral string s, convert it into its corresponding integer value.
Roman numerals are composed of the symbols:
I, V, X, L, C, D, M, representing values from 1 to 1000.

Other Topics covered : Maths, Hashmap

Approach (Reverse Traversal):
->Use a dictionary to map Roman symbols to their integer values.
->Reverse the string to process it from right to left.
->Maintain:
prev: the value of the previous symbol
summ: the cumulative total
->For each symbol:
->If the current value is less than the previous value, subtract it.
->Otherwise, add it to the total.
Time Complexity: O(n), where n is the length of the Roman numeral'''
#Python Implementation
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = (s.upper())[::-1]
        summ = 0
        prev = 0
        for i in s:
            cur = rom_dic[i]
            if cur<prev:
                summ -= cur
            else:
                summ+=rom_dic[i]
            prev = cur
        return summ
