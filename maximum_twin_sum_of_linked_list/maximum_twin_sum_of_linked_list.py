# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        my_list=[]
        while head:
            my_list.append(head.val)
            head =head.next
        print(my_list)
        n =len(my_list)
        max_num = 0
        for i in range(int(n / 2)):
            my_sum = my_list[i] + my_list[n-1-i]
            if my_sum > max_num:
                max_num=my_sum
        return max_num
        