class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = list(s)
        # for c in s:
        #     arr.append(c)
        for c in t:
            if c not in arr:
                return False
            arr.remove(c)
        if len(arr):
            return False
        return True
        
