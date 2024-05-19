class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum: int = 0
        i, j = 0, len(height) - 1

        while i != j and i < j:
            curr = min(height[i], height[j]) * (j - i)
            maximum = max(maximum, curr)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maximum