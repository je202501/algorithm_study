#https://leetcode.com/problems/design-browser-history/
class ListNode(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.current = ListNode(val=homepage)
    def visit(self, url: str) -> None:
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        return None
    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev is not None :
            self.current = self.current.prev
            steps -= 1
        return self.current.val
    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next is not None:
            self.current = self.current.next
            steps -= 1
        return self.current.val