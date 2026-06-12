class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2=list1,list2
        New_list=ListNode()
        moving=New_list
        while l1 and l2:
            if l1.val>=l2.val:
                moving.next=l2
                l2=l2.next
            else:
                moving.next=l1
                l1=l1.next
            moving=moving.next
        if l1:
            moving.next=l1
        if l2:
            moving.next=l2
        return New_list.next
