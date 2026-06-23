# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=num2=0
        mul=1
        dummy=ListNode()
        cur=dummy
        while l1:
            num1=mul*l1.val+num1
            mul=mul*10
            l1=l1.next
        mul=1
        while l2:
            num2=mul*l2.val+num2
            mul=mul*10
            l2=l2.next
        total=num1+num2
        print(total)
        if total==0:
            cur.next=ListNode(0)
        else:
            while total:
                cur.next=ListNode(total%10)
                cur=cur.next
                total=total//10
        return dummy.next