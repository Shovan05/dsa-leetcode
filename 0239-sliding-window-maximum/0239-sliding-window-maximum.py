from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()  # stores indices, values kept in decreasing order
        ans = []

        for i in range(len(nums)):
            # Step 1: remove indices from back whose values are <= current value
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Step 2: add current index
            dq.append(i)

            # Step 3: remove front index if it's out of the window
            if dq[0] <= i - k:
                dq.popleft()

            # Step 4: once window has sizek, record the max
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans