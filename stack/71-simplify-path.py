"""
Problem Description:
Given an absolute Unix-style path, simplify it to its
canonical form.

Approach:
- Traverse the path one character at a time.
- Build each directory name until a '/' is encountered.
- Use a stack to simulate the directory structure.
- Handle:
  - "."  → stay in the current directory.
  - ".." → move to the parent directory.
  - Other names (including "...", "....", etc.) →
    treat them as valid directory names.
- Construct the simplified path from the stack.

Time Complexity:
O(n)

Reason:
- Each character in the path is processed once.
- Every directory is pushed onto or popped from the stack
  at most once.

Space Complexity:
O(n)

Reason:
- The stack stores the directories present in the
  simplified path.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = ["/"]
        directory = []
        dotCount = 0
        path+="/"
        
        for i in range(1, len(path)):

            if not stack:
                stack.append("/")

            if path[i].isalnum() or path[i]=="_":
                directory.append(path[i])

            elif path[i] == ".":
                dotCount +=1
                directory.append(".")

            elif path[i] == "/":

                if ((dotCount>2 or not dotCount) and directory) or (dotCount<=2 and len(directory)!=dotCount):
                    stack.append("".join(directory))

                elif dotCount<=2 and len(directory)<=2:

                    while dotCount and stack:
                        stack.pop()
                        dotCount-=1

                directory= []
                dotCount = 0

                if stack and stack[-1]!="/":
                    stack.append("/")

        while stack and stack[-1] == "/" and len(stack)>1:
            stack.pop()    
        if not stack:
            stack.append("/")
        
        return "".join(stack)

