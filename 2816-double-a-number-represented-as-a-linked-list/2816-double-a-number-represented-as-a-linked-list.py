# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            return prev

        reversed_list = reverseList(head)
        carry = 0 
        curr, prev = reversed_list, None
        #traverse the reversed linked list 
        while curr:
            new_value = curr.val * 2 + carry
            curr.val = new_value%10
            carry = 1 if new_value>9 else 0
            prev, curr = curr, curr.next
        if carry:
            prev.next = ListNode(carry)
        result = reverseList(reversed_list)
        return result






        