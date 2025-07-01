def addBinary(self, a: str, b: str) -> str:
  p_a = len(a) - 1
  p_b = len(b) - 1
  carry = 0
  result = []
  
  # Process both strings from the end to the beginning
  while p_a >= 0 or p_b >= 0 or carry:
    # Add the current digits and carry
    carry += (int(a[p_a]) if p_a >= 0 else 0)
    carry += (int(b[p_b]) if p_b >= 0 else 0)
    # Calculate the current binary bit and update carry
    carry, v = divmod(carry, 2)
    result.append(str(v))
    p_a -= 1
    p_b -= 1
  
  # Reverse the result to get the correct order
  return "".join(result[::-1])