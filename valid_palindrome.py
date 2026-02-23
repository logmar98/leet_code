class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tmp = ""
        for c in s:
            if ('a' <= c and c <= 'z') or ('0' <= c and c <= '9'):
                tmp += c
        size = len(tmp) // 2
        i = 0
        j = -1
        while (size):
            if tmp[i] != tmp[j]:
                return False
            i += 1
            j -= 1
            size -= 1
        return True

