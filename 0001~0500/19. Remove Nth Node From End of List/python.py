# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        myList=[]
        node=head
        while node!=None:
            myList.append(node.val)
            node=node.next
        del myList[-n]

        dummy = ListNode(0)  # Create a dummy node to serve as the new head
        current = dummy  # Initialize a pointer to the dummy node
        
        for val in myList:
            current.next = ListNode(val)  # Create a new node with the value
            current = current.next  # Move the pointer to the next node
        
        return dummy.next
        

# Runtime Win:56.57%
# Memory  Win:96.67%
# I use list to handle remove problem & convert list back to linked list


