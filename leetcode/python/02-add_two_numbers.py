# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummyRoot = ListNode(0)
        lret = dummyRoot
        while l1 or l2 or carry != 0:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            sum_elem = v1 + v2 + carry 
            if sum_elem > 9:
                carry = 1
                elem = sum_elem - 10
            else:
                carry = 0
                elem = sum_elem
            lret.next = ListNode(elem)
            lret = lret.next
        return dummyRoot.next
