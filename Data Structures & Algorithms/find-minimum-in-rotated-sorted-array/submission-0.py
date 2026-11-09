class Solution:
    def findMin(self, nums: List[int]) -> int:
        low_bound = 0
        high_bound = len(nums) - 1

        minimum = low_bound

        while high_bound > low_bound:
            middle = (high_bound + low_bound) // 2

            if nums[middle] < nums[high_bound]:
                high_bound = middle
            else:
                low_bound = middle + 1


        return nums[high_bound]