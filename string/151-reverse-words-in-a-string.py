"""
Problem Description:
Given a string s, reverse the order of the words.

Requirements:
- Words are separated by one or more spaces.
- Remove leading and trailing spaces.
- The output should contain exactly one space between words.

Approach:
- Traverse the string and extract words manually.
- Ignore extra spaces.
- Store each word in an array.
- Build the answer by traversing the array in reverse order.
- Insert a single space between consecutive words.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        array = []

        temp = ""

        for i in s.strip():

            if i == " " and temp != "":
                array.append(temp)
                temp = ""

            elif i != " ":
                temp += i

        array.append(temp)

        output = array[-1]

        for i in range(len(array) - 2, -1, -1):
            output += " " + array[i]

        return output
