from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
  longest_prefix = ""
  # loop through each character of the first string
  for i, c in enumerate(strs[0]):
    # check if the character at index i is the same in all strings
    for string in strs:
      # if the index is out of bounds or the character does not match, return the longest prefix found so far
      if i >= len(string) or string[i] != c:
        return longest_prefix
    # if the character matches in all strings, add it to the longest prefix
    longest_prefix += c
  # if we reach here, it means all characters in the first string are part of the longest prefix
  return longest_prefix