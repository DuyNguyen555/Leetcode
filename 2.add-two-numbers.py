#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)
            current.next =ListNode(val)
            
            # Update
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
# @lc code=end
if __name__ == '__main__':
    lis = ListNode()
    l1 = lis.append()
    l2 = lis.append()
    l12 = Solution().addTwoNumbers(l1, l2)































# dummy = ListNode()
#         current = dummy

#         carry = 0
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             carry, value = divmod(val1 + val2 + carry, 10)
#             current.next = ListNode(value)
            
#             current = current.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
        
#         return dummy.next