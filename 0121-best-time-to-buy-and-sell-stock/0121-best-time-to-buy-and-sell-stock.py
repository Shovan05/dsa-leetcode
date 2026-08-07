class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''left=0
        right=1
        ans=[0]
        while True:
            if right == len(prices):
                break
            if prices[right]<prices[left] and right!=(len(prices)-1) :
                left=right
                right+=1
            ans.append(prices[right]-prices[left])
            right+=1
        return max(ans)'''

        ans=[]
        left=prices[0]
        for i in range (len(prices)):
            if i==0:
                ans.append(0)
            else :
                ans.append(min(left,prices[i]))
                left=min(left,prices[i])
        for i in range (1,len(ans)):
            ans[i]=prices[i]-ans[i]
        return (max(ans))
            
