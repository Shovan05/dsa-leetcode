class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen={}
        ans=[]
        flag=False
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        bucket=[[] for _ in range(len(nums)+1)]
        for i in seen:
            bucket[seen[i]].append(i)
        

        for index in range(len(bucket)-1, 0, -1):
            if flag:
                break
            for num in bucket[index]:       
                if k!=0:
                    ans.append(num)
                    k-=1
                else:
                    flag=True
                    break
        return ans     