# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        length = 0
        curr = head
        while curr is not None:
            length+=1
            curr = curr.next
        if length < 4:
            return [-1,-1]
        indices = []
        curr = head
        index = 1
        while curr.next.next is not None:
            index += 1
            if (curr.next.val > curr.val and curr.next.val > curr.next.next.val) or (curr.next.val < curr.val and curr.next.val < curr.next.next.val):
                indices.append(index)
            curr = curr.next
        if len(indices) < 2:
            return [-1,-1]
        maxDistance = indices[-1] - indices[0]
        smallestDistance = maxDistance
        for i in range (1, len(indices)):
            distance = indices[i] - indices[i-1]
            if  distance < smallestDistance:
                smallestDistance = distance
        return [smallestDistance, maxDistance]
