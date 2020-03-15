class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_index = {}  # val:idx
        for i in range(len(nums)):
            elem = target - nums[i]
            if elem in hash_index:
                return [hash_index[elem], i]
            hash_index[nums[i]] = i
        return []   
