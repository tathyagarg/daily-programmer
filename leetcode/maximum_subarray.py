class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum: int = nums[0]
        max_sum: int = nums[0]

        for num in nums[1:]:
            if num > (curr_sum + num):
                curr_sum = num
            else:
                curr_sum += num
            
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum