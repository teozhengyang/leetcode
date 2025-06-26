from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
    # start from the last digit and add one
    num_digits = len(digits)
    
    # loop through the digits in reverse order
    for i in range(num_digits - 1, -1, -1):
      # increment the current digit
      digits[i] += 1
      # modulo
      digits[i] %= 10
      # if the digit is not zero, we are done
      if digits[i] != 0:
        return digits
    
    # if we reach here, it means we have a carry
    # so we need to add a new digit at the front
    return [1] + digits
  