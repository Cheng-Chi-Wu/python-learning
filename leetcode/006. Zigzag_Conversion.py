class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        rows = [""] * numRows
        direction = 1
        cur = 0
        for i in s:
            rows[cur] += i
            if cur == numRows-1:
                direction = -1
            elif cur == 0:
                direction = 1
            cur += direction
        return "".join(rows)
