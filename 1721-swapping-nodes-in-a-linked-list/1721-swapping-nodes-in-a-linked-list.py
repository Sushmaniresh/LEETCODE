# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        data = []
        curr = head
        while curr is not None:
            data.append(curr.val)
            curr = curr.next
        data[k-1], data[-k] = data[-k], data[k-1]
        head = ListNode(data[0])
        curr = head
        for item in data[1:]:
            curr.next = ListNode(item)
            curr = curr.next
        return head



        