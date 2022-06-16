#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        
        div = 1
        while x >= div * 10:
            div *= 10
        
        while x:
            right = x % 10
            left = x // div
            if left != right: return False
            
            x = (x % div) // 10
            div /= 100
        
        return True
# @lc code=end