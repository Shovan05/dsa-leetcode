class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        temp = []

        def helper(idx):
            if idx >= n:
                res.append(temp[:])
                return

            temp.append(nums[idx])
            helper(idx + 1)

            temp.pop()
            helper(idx + 1)

        helper(0)
        return res