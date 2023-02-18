# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # split the linked list
        def splitlist(head):
            # list of size 1 never enters in this fuction
            middle = head
            tail = head.next
            while tail:
                tail = tail.next
                if tail:
                    middle = middle.next
                    tail = tail.next

            # split from middle
            a = head
            b = middle.next
            # cut the list
            middle.next = None
            return(a, b)

        # merge the linked list
        def merge(a, b):
            newlist = ListNode()
            temp = newlist
            while a and b:
                if a.val <= b.val:
                    temp.next = a
                    temp = temp.next
                    a = a.next
                else:
                    temp.next = b
                    temp = temp.next
                    b = b.next

            while a:
                temp.next = a
                temp = temp.next
                a = a.next

            while b:
                temp.next = b
                temp = temp.next
                b = b.next

            # pop the head

            return newlist.next

        # recursively sort the linked list
        def mergesort(head):
            # if the list is empty or single Node
            if head == None or head.next == None:
                return head
            # split the list
            a, b = splitlist(head)
            
            # merge after split 
            return merge(mergesort(a), mergesort(b))

        return mergesort(head)
