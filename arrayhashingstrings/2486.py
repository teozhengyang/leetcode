# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pointer = 0
        t_pointer = 0

        # loop through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # advance both pointers if match
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            # advance s_pointer if no match
            else:
                s_pointer += 1
        
        # return the number of unmatched characters in t
        return len(t) - t_pointer