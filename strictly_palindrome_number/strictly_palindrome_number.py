def convert_to_base_n(num,base):
    result = ''
    while num > 0:
        result = str(num % base) + result
        num //= base
    return result


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        is_strict_palindrome=True
        for i in range (2, n-1):
            result = convert_to_base_n(n,i)
            if (result != result[::-1]):
                is_strict_palindrome=False
                break
        return is_strict_palindrome
        