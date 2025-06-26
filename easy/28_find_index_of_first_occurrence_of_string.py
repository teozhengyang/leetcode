def strStr(self, haystack: str, needle: str) -> int:
  needle_length = len(needle)
  haystack_length = len(haystack)
  
  # loop through the haystack
  for i in range(haystack_length - needle_length + 1):
    # Check if the substring matches the needle
    if haystack[i:i + needle_length] == needle:
      return i