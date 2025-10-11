# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.startswith('-') and len(token) > 1:
                stack.append(int(token[1:]) * -1)
            elif token.isdigit():
                stack.append(int(token))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                if token == '+':
                    stack.append(first_operand + second_operand)
                elif token == '-':
                    stack.append(first_operand - second_operand)    
                elif token == '*':
                    stack.append(first_operand * second_operand)
                else:
                    stack.append(int(first_operand / second_operand))
        
        return stack[0]