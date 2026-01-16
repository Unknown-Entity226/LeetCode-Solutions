'''
Problem Description:
Given an array of strings, return the longest common prefix
shared among all strings.
If there is no common prefix, return an empty string "".
Approach:
- The longest possible prefix cannot be longer than the shortest string.
- Iterate character by character over the shortest string.
- For each character position, check whether all strings have the same character at that index.
- If all match, append the character to the result.
- Stop immediately when a mismatch is found.
Time Complexity: O(n * m), n = number of strings and m = length of the shortest string
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common =""
        i =0
        count=0
        smallest = min(strs, key=len)
        print(smallest)
        while i<len(smallest):
            stored = smallest[i]
            print(stored)
            for string in strs:
                if string[i] ==  stored:
                    count+=1
            if count==len(strs):
                common+=stored
                print(common)
                i+=1
                count =0
            else:
                break
        return common
        

