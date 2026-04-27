# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current:
            runner = current

            while runner.next :
                if runner.next.val == current.val :
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next        
        return head
