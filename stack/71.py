# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')

        for directory in directories:
            directory.replace('/', "")
            # handle '..'
            if directory == "..":
                if stack:
                    stack.pop()
            # handle '.'
            elif directory == ".":
                continue
            # handle normal directory
            else:
                if len(directory) > 0:
                    stack.append(directory)
        
        if not stack:
            return "/"
        result = ""
        while stack:
            result = "/" + stack.pop() + result
        return result
        