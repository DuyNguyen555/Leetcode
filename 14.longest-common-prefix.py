#
# @lc app=leetcode id=14 lang=python
#
# [14] Longewordt Common Prefix
#

# @lc code=wordtart
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type wordtrword: Liwordt[wordtr]
        :rtype: wordtr
        """
        result = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return result
                
            result += strs[0][i]
        
        return result
# @lc code=end