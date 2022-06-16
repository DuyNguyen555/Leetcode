#
# @lc app=leetcode id=1232 lang=python
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        slope = None
        for (x1, y1), (x2, y2) in zip(coordinates, coordinates[1:]):
            if x1 == x2:
                sl = float('inf')
            else:
                sl = (y2 - y1) / (x2 - x1)
            
            if slope is None:
                slope = sl
            else:
                if slope != sl:
                    return False
        
        return True
    
    def checkStraightLine(self, coordinates):
        for (x1, y1), (x2, y2), (x3, y3) in zip(coordinates, coordinates[1:], coordinates[2:]):
            if (y2 - y1)*(x3 - x2) != (y3 - y2)*(x2-x1):
                return False
        
        return True
    
    def checkStraightLine(self, coordinates):
        (x0, y0), (x1, y1) = coordinates[:2]
        # (x1 - x0) / (y1 - y0) = (x - x1) / (y - y1)
        return all((x1 - x0)*(y - y1) == (x - x1)*(y1 - y0) for x, y in coordinates[2:])
    
# @lc code=end