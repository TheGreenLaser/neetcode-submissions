class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_bound = 0
        high_bound = len(nums) - 1
        
        while high_bound >= low_bound:
            middle = (high_bound + low_bound) // 2
            left_diff = nums[middle] - target
            right_diff = nums[high_bound] - target

            if nums[middle] == target:
                return middle

            if left_diff >= 0 or right_diff >= 0:
                if left_diff >= 0 and not right_diff >= 0:
                    high_bound = middle
                    continue
                if right_diff >= 0 and not left_diff >= 0:
                    low_bound = middle + 1
                    continue

            if left_diff < right_diff:
                high_bound = middle
            else:
                low_bound = middle + 1

        return -1