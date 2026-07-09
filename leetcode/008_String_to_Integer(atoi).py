class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        sign = 1
        
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s):
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1
        
        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i += 1
        res *= sign
        if res < -2**31: res = -2**31
        if res > 2**31-1: res = 2**31-1
        return res