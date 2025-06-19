# string method

def isPalindrome(self, x: int) -> bool:
    x_str = str(x)
    left = 0
    right = len(x_str) - 1
    # compare characters from both ends towards the center
    while left <= right:
        if x_str[left] != x_str[right]:
            return False
        left += 1
        right -= 1
    return True

# numeric method
# construct reverse half of the number and compare it with the original number
def isPalindrome(self, x: int) -> bool:
    # negative numbers and multiples of 10 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    # even length: x == reversed_half
    # odd length: x == reversed_half // 10 (remove the middle digit)
    return x == reversed_half or x == reversed_half // 10