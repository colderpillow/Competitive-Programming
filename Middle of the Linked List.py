# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        pointer = head
        temp = head
        while(pointer != None):
            pointer = pointer.next
            counter += 1
        for i in range(int(counter/2)):
                head = head.next
                temp = head
        return temp
