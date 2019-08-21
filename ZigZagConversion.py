# Created by Jack Brewer August 2019

# Description
# Convert a string into zigag format with a given number of rows
# Example: The string "PAYPALISHIRING" is written in a zigzag pattern on 3 rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Strategy
# Need to build string row by row. The first and last row have constant 
# distance between each index, while the interior rows vary based on the current row
# Only requires one traversal, and storage for the returned zigzag string

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        word = ""
        counter = 0
        
        if(numRows == 1):
            return s
        
        for row in range(numRows):
            counter = row
            while(counter < len(s)):
                word += s[counter]

                if(row == 0 or row == numRows - 1):
                    counter += (numRows * 2) - 2
                
                else:
                    if(counter + (numRows*2) - 2 - (row * 2) < len(s)):
                        word+= s[counter + ((numRows*2) - 2) - (row * 2)]
                    counter += (numRows * 2) - 2
                
        return word
