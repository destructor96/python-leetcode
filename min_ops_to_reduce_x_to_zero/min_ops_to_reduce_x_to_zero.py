class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total - x
        if target == 0:  # if the sum of all elements is x
            return len(nums)

        left, right, currentSum, maxLength = 0, 0, 0, float('-inf')

        while right < len(nums):
            currentSum += nums[right]
            right += 1

            while currentSum > target and left < right:
                currentSum -= nums[left]
                left += 1

            if currentSum == target:
                maxLength = max(maxLength, right - left)

        if maxLength != float('-inf'):
            return len(nums) - maxLength
        else:
            return -1


# main
if __name__ == '__main__':
    # Test cases
    x = 5
    nums = [1,1,4,2,3]
    test = Solution()
    print(test.minOperations(nums, x))