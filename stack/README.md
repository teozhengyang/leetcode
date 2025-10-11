# Stack

- Keep track of previous elements with current element (LIFO order)
- Nested/hierarchical structures (parentheses, expressions)
- Next/previous greater/smaller element (monotonic stack)
- Revisit element in reverse order

```
# Parentheses
stack = []
for c in s:
    if c in open_brackets:
        stack.append(c)
    else:  # closing
        if not stack or not matches(stack[-1], c):
            return False
        stack.pop()
return not stack
```

```
# Monotonic Stack
stack = []
for i, num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        idx = stack.pop()
        result[idx] = num
    stack.append(i)
```

```
# Expression
stack = []
for token in tokens:
    if token is number:
        stack.append(int(token))
    else:
        b, a = stack.pop(), stack.pop()
        stack.append(apply_op(a, b, token))
return stack[-1]
```

| **Question Mentions / Keywords**     | **Window Type**              | **Movement Logic**                                             | **Example Problem**                       |
| ------------------------------------ | ---------------------------- | -------------------------------------------------------------- | ----------------------------------------- |
| “Balanced”, “Valid”, “Parentheses”   | Stack of chars               | Push open; pop on close; verify empty at end                   | Valid Parentheses (LC 20)                 |
| “Previous/Next greater/smaller”      | Monotonic stack              | Maintain increasing/decreasing stack; pop when condition fails | Daily Temperatures, Next Greater Element  |
| “Undo”, “Evaluate”, “Postfix”, “RPN” | Expression evaluation stack  | Push operands; pop two when operator seen                      | Evaluate Reverse Polish Notation (LC 150) |
| “Decode”, “Nested”, “Expand”         | Stack of substrings/counts   | Push on `[`, pop on `]` to reconstruct string                  | Decode String (LC 394)                    |
| “Asteroids”, “Collide”, “Buildings”  | Simulation / collision stack | Pop until resolved or append                                   | Asteroid Collision (LC 735)               |
| “Histogram”, “Largest Rectangle”     | Monotonic increasing stack   | Pop when height decreases; compute width on pop                | Largest Rectangle in Histogram (LC 84)    |
| “Next/Previous element pattern”      | Monotonic stack              | Track indices for efficient range calculations                 | Trapping Rain Water (LC 42)               |

# Questions

- [71. Simplify Path](https://leetcode.com/problems/simplify-path) 
- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation)
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures)