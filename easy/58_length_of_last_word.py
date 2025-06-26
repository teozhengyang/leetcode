def lengthOfLastWord(self, s: str) -> int:
  # find end of last word
  end = len(s) - 1
  while end >= 0 and s[end] == ' ':
    end -= 1
    
  # find start of last word
  start = end
  while start >= 0 and s[start] != ' ':
    start -= 1
  
  return end - start