class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        Roman = [
            'M', "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
            ]
        for i in range(len(values)):
            while num >= values[i]:
                ans += Roman[i]
                num -= values[i]
        
        return ans