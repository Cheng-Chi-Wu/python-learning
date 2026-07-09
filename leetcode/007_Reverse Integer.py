class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1 
        x = abs(x)
        res = int(str(x)[::-1]) * sign
        if res < -2**31 or res > 2**31-1:
            return 0
        return res