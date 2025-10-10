# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # frequency dict of t
        freq_t = Counter(t)
        # sliding window for s
        freq_s = {}
        # left pointer for s
        left = 0
        # tracker for whether s's window fits t
        counter = 0
        # result
        result = -1
        length = float('inf')

        for i in range(len(s)):
            # update sliding window
            if s[i] in freq_s:
                freq_s[s[i]] += 1
            else:
                freq_s[s[i]] = 1
            
            # update tracker
            if s[i] in freq_t and freq_s[s[i]] == freq_t[s[i]]:
                counter += 1
            
            # update result
            while left <= i and counter == len(freq_t):
                if length > i - left + 1:
                    length = i - left + 1
                    result = left
                # advance left pointer
                freq_s[s[left]] -= 1
                if s[left] in freq_t and freq_s[s[left]] < freq_t[s[left]]:
                    counter -= 1
                left += 1
        
        if result == -1:
            return ""
        return s[result:result+length]
