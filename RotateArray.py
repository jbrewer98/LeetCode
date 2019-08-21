# Created by Jack Brewer August 2019

# Description
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Strategy
# Rotate the array in place in one traversal. Operate on cycles that depend on
# the size of the array and the shift length. Start at first index, store the value of
# the index to be overwritten, override that value, and shift. Continue until the start index is
# reached again, at which point a new cylce starts. Requires no copying of the array and only
# one traversal.

class RotateArray:
    def rotate(self, nums: List[int], k: int) -> None:
        if(k == 0 or len(nums) == 0):
            return
        
        k = k % len(nums)
        curIndex = k
        count = 0
        start = 0
        started = False
        
        while(count < len(nums)):
            tempVal = nums[start]

            while(curIndex != start or not started):
                started = True
                valueToReplace = nums[curIndex]
                nums[curIndex] = tempVal
                tempVal = valueToReplace
                curIndex = (curIndex + k) % (len(nums))
                
                count += 1
                
            nums[curIndex] = tempVal
            count+=1
            start += 1
            curIndex = start + k % len(nums)
            started = False
