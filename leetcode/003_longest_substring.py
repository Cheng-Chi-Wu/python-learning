class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        start = 0
        ans = 0
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
                
            seen.add(s[end])
            ans = max(ans, end - start+1)
        return ans
             