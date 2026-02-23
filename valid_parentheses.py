class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for p in s:
            if p == "(" or p == "{" or "[" == p:
                arr.append(p)
            else:
                if not len(arr):
                    return False
                match p:
                    case ")":
                        if arr[-1] != "(":
                            return False
                    case "}":
                        if arr[-1] != "{":
                            return False
                    case "]":
                        if arr[-1] != "[":
                            return False
                arr.pop()
        if len(arr):
            return False
        return True
