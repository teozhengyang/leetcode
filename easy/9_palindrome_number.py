def isPalindrome(self, x: int) -> bool:
    # negative numbers and multiples of 10 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        # append the last digit of x to reversed_half
        reversed_half = reversed_half * 10 + x % 10
        # remove the last digit from x
        x //= 10
    # even length: x == reversed_half
    # odd length: x == reversed_half // 10 (remove the middle digit)
    return x == reversed_half or x == reversed_half // 10