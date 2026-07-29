class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        smallest = prices[0]
        descending = True
        
        if(len(prices) <= 1):
            return 0

        for i in range(len(prices)):
            smallest = min(smallest, prices[i])
            ret = max(prices[i] - smallest, ret)

            if i > 0:
                if prices[i] > prices[i-1]:
                    descending = False
        
        if descending:
            return 0

        return ret
            

        
            

