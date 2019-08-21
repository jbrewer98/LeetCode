# Created by Jack Brewer August 2019

# Description
# Given a string, find the length of the longest substring without repeating characters.

# Strategy
# Iterate through the string letter by letter, while keeping a substring with the current unique string.
# Check if each letter is in the unique string, if it is then remove all letters up until the first instance.
# If not, then add the letter to the substring and update maxlength

class LongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        tempStr = ""
        
        for let in s:
            # If letter is in the current string, remove all letters to first instance
            while(let in tempStr):
                tempStr = tempStr[1:]
                
            # Add letter to current string and update max length
            tempStr += let
            if(len(tempStr) > maxLength):
                maxLength = len(tempStr)     
        
        return maxLength
