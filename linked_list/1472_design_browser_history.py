'''
Problem Description:
You have a browser with a single tab that starts at the homepage.
You can:
- Visit a new URL
- Move back in history by a given number of steps
- Move forward in history by a given number of steps

When visiting a new page:
- All forward history is cleared.

Implement the BrowserHistory class with the following methods:
- BrowserHistory(homepage): Initializes the browser with the homepage.
- visit(url): Visits a new URL.
- back(steps): Moves back by at most 'steps' steps and returns the current URL.
- forward(steps): Moves forward by at most 'steps' steps and returns the current URL.

Approach:
- Use a doubly linked list to represent browser history.
- Each node stores:
  - url: the current page
  - prev: pointer to the previous page
  - next: pointer to the next page
- Maintain a pointer (current) to the current page.

Operations:
- visit:
  - Clear forward history by setting current.next to None.
  - Create a new node and link it after the current node.
  - Move the current pointer to the new node.
- back:
  - Move the current pointer backward up to 'steps' times
    or until no previous page exists.
- forward:
  - Move the current pointer forward up to 'steps' times
    or until no next page exists.

Time Complexity:
- visit: O(1)
- back: O(steps)
- forward: O(steps)
'''

class Node:
    def __init__(self, url, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.homepage = Node(homepage)
        self.current = self.homepage

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.current.next = None
        new = Node(url, None, self.current)
        self.current.next = new
        self.current = new

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current.next is not None:
            self.current = self.current.next
            steps -= 1
        return self.current.url
