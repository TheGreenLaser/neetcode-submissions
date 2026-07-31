class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while(upper >= lower):
            index = (upper + lower) // 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                lower = index + 1
            else:
                upper = index - 1

        return -1

