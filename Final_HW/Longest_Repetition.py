# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(num_list):
    i = 0
    count = 0
    if len(num_list) == 0:
        return None
    ref_element = num_list[0]
    ref_max = 1
    temp_element = num_list[0]
    temp_max = 1
    
    for element in num_list:  
        if temp_element  == element:
            count = count + 1
            temp_max = count
            if temp_max > ref_max:
                ref_max = temp_max
                ref_element = element                  
        else:
            temp_element = element
            count = 1

    return ref_element
    


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

