#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
# @lc code=end























        # Case 1:
        # cur = head
        # while cur:
        #     while cur.next and cur.next.val == cur.val:
        #         cur.next = cur.next.next
        #     cur = cur.next
        
        # return head