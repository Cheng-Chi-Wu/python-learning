class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a,b = nums1, nums2
        if len(a) > len(b): 
            a, b = b, a
        m, n = len(a), len(b)
        total = m + n
        half = (total+1)//2
        left = 0 
        right = m
        while left <= right:
            i = (left+right) // 2
            j = half - i

            Aleft = a[i-1] if i > 0 else float("-inf")
            Aright = a[i] if i < m else float("inf")
            Bleft = b[j-1] if j > 0 else float("-inf")
            Bright = b[j] if j < n else float("inf")

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 1:
                    return max(Aleft, Bleft)
                
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2.0

            if Aleft > Bright:
                right = i -1
            else:
                left = i + 1