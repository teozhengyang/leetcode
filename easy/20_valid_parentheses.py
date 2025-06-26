def isValid(self, s: str) -> bool:
  # create stack using list
  stack = []
  valid_pairs = set('()', '[]', '{}')
  
  # loop through string
  for c in s:
    # add to stack if opening parentheses
    if c in '([{':
      stack.append(c)
    # check stack if closing parentheses (stack cannot be empty or invalid pairs)
    elif not stack or stack.pop() + c not in valid_pairs:
      return False
  # empty stack = all valid pairs
  return not stack