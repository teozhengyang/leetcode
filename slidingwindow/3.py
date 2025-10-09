# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_map = {}
        length = 0
        start = 0

        for i in range(len(s)):
            # add new char to window
            if s[i] in freq_map:
                freq_map[s[i]] += 1
            else:
                freq_map[s[i]] = 1
            # advance left pointer if duplicates of current char found
            while freq_map[s[i]] > 1:
                freq_map[s[start]] -= 1
                start += 1
            # update length
            length = max(length, i - start + 1)

        return length