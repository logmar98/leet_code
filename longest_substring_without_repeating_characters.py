class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        arr = []
        i = 0
        s = list(s)
        while i < len(s):
            if s[i] not in arr:
                arr.append(s[i])
                i += 1
            else:
                arr.clear()
                tmp = s[i]
                for x in list(s):
                    s.pop(0)
                    if x == tmp:
                        break
                i = 0
            if result < len(arr):
                result = len(arr)
        return result
        
