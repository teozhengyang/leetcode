# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')

        for directory in directories:
            directory.replace('/', "")
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or not directory:
                continue
            else:
                stack.append(directory)
        
        if not stack:
            return "/"
        return "/" + "/".join(stack)
        