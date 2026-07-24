class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hSet = set()

        for num in nums:
            if num in hSet:
                return True
            else:
                hSet.add(num)

        return False
        