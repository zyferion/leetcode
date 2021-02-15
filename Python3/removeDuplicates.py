# Problem 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    
    # Initiate index
    i = 0
    
    # Only loop until last element 
    while (i < len(nums)-1):
        
        # Store element to check
        elem = nums[i]
        
        # If element is same as next element, delete current element
        if elem == nums[i+1]:
            
            del nums[i]
        
        # Else go to next element in list
        else:
            i = i+1
        
    return(len(nums))
