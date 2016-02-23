# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

def next_row(current_row):
    result = [1]
    i = 1
    while i< len(current_row):
        result = result + [current_row[i-1]+current_row[i]]
        i = i + 1
    return result + [1]
    

def triangle(n):
    result = [[1] ]   
    if n == 0:
        return []
    current_row = [1]
    i = 1
    while i < n:
        result = result + [next_row(current_row)]
        current_row = next_row(current_row)
        i = i + 1
    return result

################following is too complecated###################
def triangle(n):
    result = []
    
    if n == 0:
        return []
    if n == 1:
        return [[1]]

##############
    i = 0
    j = 0
    num_list = []
    while j<n:
        num_list.append(1)
        j=j+1
    
    while i < n:
        if i < n-1 and i>0: # i in the middle
            num_list[i] = triangle(n-1)[n-2][i-1]+triangle(n-1)[n-2][i]           
        i = i + 1
    final_result = triangle(n-1) + [num_list]
    return final_result
##############################################################

#######following is wrong###########################
def triangle(n):
    result = []
    
    if n <=1:
        if n == 1:
            result.append([1])       
        else:
            result.append([])
        return result
##############
    i = 0
    j = 0
    num_list = []
    while j<n:
        num_list.append(1)
        j=j+1
    
    while i < n:
#        print i
        if i < n-1 and i>0: # i in the middle
            num_list[i] = triangle(n-1)[n-2][i-1]+triangle(n-2)[n-1][i]           
        i = i + 1
    print num_list  
    return triangle(n-1).append(num_list)
####################################################


#For example:
print triangle(0)
#>>> []
print triangle(1)
#>>> [[1]]
print triangle(2)
#>> [[1], [1, 1]]
print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
