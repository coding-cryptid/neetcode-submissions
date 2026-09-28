from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # Loop through and check if "i + complement = target"
        for i, num in enumerate(nums): 
            complement = target - num
        # Check if complement is in seen and return the indices
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
