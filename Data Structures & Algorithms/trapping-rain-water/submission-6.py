class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) -1 

        lheight = 0
        rheight = 0

        answer = 0

        if len(height) == 0:
            return 0

        while height[p1] == 0:
            if p1 >= len(height) - 1:
                break
            p1 += 1
        
        while height[p2] == 0:
            if p2 <= 0:
                break
            p2 -= 1

        lheight = height[p1]
        rheight = height[p2]

        while p1 < p2:
            if rheight > lheight:
                p1 += 1

                if height[p1] > lheight:
                    lheight = height[p1]
                else:
                    answer += lheight - height[p1]
            else:
                p2 -= 1

                if height[p2] > rheight:
                    rheight = height[p2]
                else:
                    answer += rheight - height[p2]

            

        return answer

        
