class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nDict = {}
        for i in range(len(nums)):
            need = target - nums[i]

            if need in nDict:
                return [nDict[need], i]

            nDict[nums[i]] = i

        return [0, 0]

