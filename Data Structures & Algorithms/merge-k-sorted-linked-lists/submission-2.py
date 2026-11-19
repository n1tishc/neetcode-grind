# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        heap = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next

            if node:
                heapq.heappush(heap, (node.val, idx, node))
        return dummy.next