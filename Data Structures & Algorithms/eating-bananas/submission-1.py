class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Initial bounds: [1, size of biggest pile]
        #Binary search:
            #Go through array and calculate total time
            #Find minimum

        bound_left = 1
        bound_right = 1

        for i in piles:
            bound_right = max(i, bound_right)

        minimum_k = math.inf
        
        while bound_right >= bound_left:
            cur_k = (bound_left+bound_right) // 2
            total_time = 0

            for i in piles:
                total_time += math.ceil(i / cur_k)

            if total_time > h:
                bound_left = cur_k + 1
            elif total_time <= h:
                minimum_k = min(minimum_k, cur_k)
                bound_right = cur_k - 1

        return minimum_k


            

