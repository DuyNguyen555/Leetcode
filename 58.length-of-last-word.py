#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
    
    def lengthOfLastWord(self, s):
        if not s: return 0

        i, length = len(s) - 1, 0
        while s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length
# @lc code=end