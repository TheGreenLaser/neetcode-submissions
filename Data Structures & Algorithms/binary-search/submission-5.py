class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = (len(nums)) // 2

        lower = 0
        upper = len(nums) - 1

        if nums[index] == target:
            return index

        while(upper >= lower):
            if nums[index] == target:
                return index
            elif nums[index] < target:
                lower = index + 1
            else:
                upper = index - 1

            index = (upper - lower) // 2 + lower

        return -1

