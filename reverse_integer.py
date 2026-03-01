class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x *= -1
        s = str(x)
        i = -1
        result = ""
        while i >= -len(s):
            result += s[i]
            i -= 1
        n = int(result) * flag
        if n < -2 ** 31 or n > 2 ** 31 - 1:
            return 0
        return n
