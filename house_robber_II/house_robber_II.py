class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)

        # If there's only one or two houses, return the max of what's there
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Helper function to compute max rob for a linear list
        def linearRob(nums):
            rob_prev, rob_curr = 0, 0
            for num in nums:
                rob_prev, rob_curr = rob_curr, max(rob_prev + num, rob_curr)
            return rob_curr

        # Using the helper function for both scenarios
        return max(linearRob(nums[:-1]), linearRob(nums[1:]))

