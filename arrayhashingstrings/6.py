# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # base case
        if numRows == 1:
            return s
        
        # create 2D array to store rows    
        result = [[] for _ in range(numRows)]
        counter = 0
        reverse = False

        for c in s:
            # add char to the current row
            result[counter].append(c)
            # reverse once at last row
            if counter == numRows - 1:
                reverse = True
                counter -= 1
            # stop reverse once at first row
            elif counter == 0:
                reverse = False
                counter += 1
            # update counter based on reverse
            elif reverse:
                counter -= 1
            else:
                counter += 1
        
        # concatenate all rows
        result_string = ""
        for row in result:
            result_string += (''.join(row))
        
        return result_string
        
        

        