class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        ans = 0
        maxh = max(height)
        while left < right:
            mheight = min(height[left], height[right])
            area = mheight * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if maxh*(right-left) < ans:
                break

        return ans