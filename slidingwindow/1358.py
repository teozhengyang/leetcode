# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq_list = [0, 0, 0]
        result = 0
        left = 0

        for i in range(len(s)):
            # update sliding window
            freq_list[ord(s[i]) - ord('a')] += 1
            # update result
            while all(freq_list):
                # add all substrings from valid left position
                result += len(s) - i
                # advance left pointer to find new substrings
                freq_list[ord(s[left]) - ord('a')] -= 1
                left += 1
        
        return result