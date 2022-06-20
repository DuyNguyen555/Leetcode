#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "": return 0
        
        if needle in haystack:
            return haystack.index(needle)
        
        return -1
    
    def strStr(self, haystack, needle):
        if needle == "": return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+ len(needle)] == needle:
                return i
        
        return -1
# @lc code=end