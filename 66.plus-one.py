#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        one, length = 1, 0
        while one:
            if length < len(digits):
                if digits[length] == 9:
                    digits[length] = 0
                else:
                    digits[length] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
                
            length += 1
        
        return digits[::-1]
# @lc code=end