class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1

        ret = 0

        while p1 < p2:
            ret = max(ret, (p2 - p1) * min(heights[p2], heights[p1]))
            if heights[p2] < heights[p1]: p2 -= 1
            else: p1 += 1
        
        return ret