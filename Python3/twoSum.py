# Problem 1: TwoSum
# https://leetcode.com/problems/two-sum/

# Solution

def twoSum(nums, target):

    index_list = list(range(len(nums)))
    
    for i in index_list:
        
        index_1 = index_list[i]
        index_2 = index_list[i] + 1

        while index_2 <= index_list[-1]:

            value = nums[index_1] + nums[index_2]
            
            if value == target:
                return([index_1,index_2])
            
            else:
                index_2 = index_2 + 1
