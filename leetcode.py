from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        c = [0] * n
        result.append(nums[:])

        i = 0
        while i < n:
            if c[i]:
                pass