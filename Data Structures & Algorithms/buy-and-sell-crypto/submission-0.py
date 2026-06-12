class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #int array prices, day 2 > day 1
        #return max profit, u can make 0 transactions if needed

        max_p = 0
        min_price = 101

        for price in prices:
            if price < min_price:
                min_price = price
            
            if price - min_price > max_p:
                max_p = price - min_price
        
        return max_p
    

        
        
