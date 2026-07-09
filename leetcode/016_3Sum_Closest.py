class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n-2):
            l = i + 1
            r = n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
                
        return closest