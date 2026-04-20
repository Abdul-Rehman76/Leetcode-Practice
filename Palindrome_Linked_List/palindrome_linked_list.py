# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return
        my_stack=[]
        while(head):
            my_stack.append(head.val)
            head = head.next
        
        return my_stack == my_stack[::-1]
        