# Problem 2 
# https://leetcode.com/problems/add-two-numbers/

def addTwoNumbers(l1, l2):
    
    l1.reverse()
    l2.reverse()
    
    num_1 = int(''.join([str(elem) for elem in l1]))
    num_2 = int(''.join([str(elem) for elem in l2]))
    
    sum_result = list(str(num_1+num_2))
    
    sum_result.reverse()
    
    return([int(elem) for elem in sum_result])
    
