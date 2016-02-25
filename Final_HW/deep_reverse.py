# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

        
def deep_reverse(p):
    i = len(p)
    result = []
    
    while i > 0:
        result.append(p[i-1])
        i = i - 1
        
    j = 0  
    while j < len(result):
        if is_list(result[j]):
            result[j] = deep_reverse(result[j])
        j = j + 1
    return result

# spent a lot time doing this. The reseaon is I didnt change the value
# of result[j] in the while loop. I used for-loop and 
# element =  deep_reverse(element), which didnt change the result of result.


##########solution###########

def deep_reverse(p):
    if is_list(p):
        result = []
        for i in range( len(p) - 1, -1, -1):
            result.append(deep_reverse(p[i]))
        return result
    else:
        return p


#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]
