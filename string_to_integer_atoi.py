class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        j = 0
        sign = 1
        num = ""
        n = len(s)
        if n == 0:
            return 0
        while i < n and s[i].isspace():
            i += 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign *= -1
            i += 1
        while i < n and '0' <= s[i] and s[i] <= '9':
                num += s[i]
                i += 1
        if len(num) == 0:
            return 0
        result = int(num)
        result *= sign
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result

