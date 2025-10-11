# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # append numbers
            if token.isdigit():
                stack.append(int(token))
            elif token.startswith('-') and token[1:].isdigit():
                stack.append(int(token[1:]) * -1)
            # perform operations
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                result = None
                if token == '+':
                    result = first_num + second_num
                elif token == '-':
                    result = first_num - second_num
                elif token == '*':
                    result = first_num * second_num
                else:
                    result = int(first_num / second_num)
                stack.append(result)
        
        return stack[0]