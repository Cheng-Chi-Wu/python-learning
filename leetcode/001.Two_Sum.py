class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        ans = []
        for i, num in enumerate(nums):
            if target - num in hashmap:
                ans = [hashmap[target-num], i]
                break
            hashmap[num]=i
        return ans