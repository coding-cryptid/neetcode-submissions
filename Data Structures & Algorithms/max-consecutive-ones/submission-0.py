class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_streak = 0
        for i in nums:

            if i == 1:
                current_streak = current_streak + 1
                max_streak = max(max_streak, current_streak)
            elif i == 0:
                current_streak = 0
        return max_streak