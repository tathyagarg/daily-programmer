class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        needed = {}
        for i, num in enumerate(nums):
            if target - num in needed:
                return [i, needed[target - num]]

            needed[num] = i
