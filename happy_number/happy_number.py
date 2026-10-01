class Solution:
    def isHappy(self, n: int) -> bool:
        prev_result = []
        while(True):
            num_str=str(n)
            result = 0
            for num in num_str:
                result += (int(num))**2
            if result in prev_result:
                return False
            else:
                prev_result.append(result)
            if result == 1:
                return True
            else:
                n = result
            
            
            