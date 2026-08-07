class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min=prices[0]
        max=0
        for price in prices:
            if price<min:
                min=price
            profit=price-min
            if profit>max:
                max=profit
        return max
            
