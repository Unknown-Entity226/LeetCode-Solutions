"""
Problem Description:
Implement the atoi() function to convert a string into a
32-bit signed integer following the specified parsing
rules.

Approach:
- Skip leading whitespaces.
- Determine the sign if '+' or '-' is present.
- Ignore leading zeros.
- Read consecutive digits to build the integer.
- Stop when a non-digit character is encountered.
- Clamp the final value to the 32-bit signed integer
  range.

Time Complexity:
O(n)

Reason:
- The string is traversed at most once.
- Each character is processed once.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -1*(2**31)
        INT_MAX = (2**31)-1
        sign = 1
        number = 0
        encounter = False
        signdone = False
        for i in s:
            if sign*number<INT_MIN:
                return INT_MIN
            if sign*number>INT_MAX:
                return INT_MAX
            if  i == " ":
                if not encounter and not signdone:

                    continue
                else:
                    break
            elif encounter and (i == "-" or i == "+"):
                break
            elif not number and not encounter and not signdone and i == "-":
                sign = -1
                signdone =True
            elif not number and not encounter and not signdone and i == "+":
                sign = 1
                signdone = True
            elif not number and i == "0":
                number = 0
                if not encounter:
                    encounter = True

            elif i.isdigit():
                number = number*10+int(i)
                encounter = True
            elif not i.isdigit():
                break
        result  = sign*number
        if result<INT_MIN:
            return INT_MIN
        if result>INT_MAX:
            return INT_MAX
        return result
