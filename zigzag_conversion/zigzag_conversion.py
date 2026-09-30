class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2 or len(s) < 2:
            return s
        arr = [""] * numRows
        direction = 1
        index = 0
        for character in s:
            arr[index]= arr[index]+character
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index +=direction
        s_new=""
        for string in arr:
            s_new += string
        return s_new