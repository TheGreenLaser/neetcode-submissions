class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hDict = set()

        for num in nums:
            if num in hDict:
                return True
            else:
                hDict.add(num)

        return False
        