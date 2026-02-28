class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = []
        i = 0
        while i < numRows:
            arr.append("")
            i += 1
        row = 0
        flag = 1
        for i in s:
            if row == numRows - 1:
                flag = 0
            elif row == 0:
                flag = 1

            if flag:
                arr[row] += i
                row += 1
            else:
                if row != numRows:
                    arr[row] += i
                row -= 1

        result = ""
        for x in arr:
            result += x
        return result
