class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        temp = []
        if target not in nums:
            return temp
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    temp.append(nums.index(nums[i]))
                    nums[i] = nums[i] * -1
                else:
                    continue
        return temp
