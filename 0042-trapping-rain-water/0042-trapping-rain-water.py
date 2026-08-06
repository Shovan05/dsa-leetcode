class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_pre=[]
        max_post=[0]*len(height)
        ans=0
        for i in range(len(height)):
            if i==0:
                max_pre.append(0)
            else:
                max_pre.append(max(height[i-1],max_pre[i-1]))

        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                max_post[i]=0
            else:
                max_post[i]=max(height[i+1],max_post[i+1])

        for i in range(len(height)):
            if (min(max_pre[i],max_post[i])-height[i])<0:
                ans+=0
            else:
                ans+= min(max_pre[i],max_post[i])-height[i]
        
        return ans

        
        