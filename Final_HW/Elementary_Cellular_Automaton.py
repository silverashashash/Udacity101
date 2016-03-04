# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton

# Please see the video for additional explanation.

# A one-dimensional cellular automata takes in a string, which in our 
# case, consists of the characters '.' and 'x', and changes it according 
# to some predetermined rules. The rules consider three characters, which 
# are a character at position k and its two neighbours, and determine 
# what the character at the corresponding position k will be in the new 
# string.

# For example, if the character at position k in the string  is '.' and 
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up 
# '..x' in the table below. In the table, '..x' corresponds to 'x' which 
# means that in the new string, 'x' will be at position k.

# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142

# To calculate the patterns which will have the central character x, work 
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.

# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all 
# lead to an 'x' in the next line and the rest have a '.'

# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)

# Note that the first position of the string is next to the last position 
# in the string.

# Define a procedure, cellular_automaton, that takes three inputs: 
#     a non-empty string, 
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and 
#     a positive integer, n, which is the number of generations. 
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.

def dot_to_num(string):
    n = len(string)
    number_string = []
    for e in range(0, n-1):
        number_string.append(string[e - 1] + string[e] + string[e + 1])      
    number_string.append(string[n - 2] + string[n - 1] + string[0])
    return number_string

def convert_dot_to_number_list(number_string):
    num_list = []
    patter = {'...':1, '..x':2, '.x.':4, '.xx':8, 'x..':16, 'x.x':32, 'xx.':64, 'xxx':128}
    for element in number_string:
        num_list = num_list + [patter[element]]
    return num_list

def binary(pn):
    patter_number_list = []
    m = 128 
    while m >= 1:
        if pn >= m:
            patter_number_list.append([m,1])
            pn = pn - m
        else:
            patter_number_list.append([m,0])
        m = m / 2
    pattern_dic = {}
    for element in patter_number_list:
        pattern_dic[element[0]] =  element[1]
    return pattern_dic

    
def cellular_automaton(string, pn, gn):
    i = 0
    while i < gn:
        result = ''
        number_string = dot_to_num(string)
        num_list = convert_dot_to_number_list(number_string)
        pattern_dic = binary(pn)
        
        for element in num_list:
            if pattern_dic[element] == 1:
                result = result + 'x'
            else:
                result = result + '.'
        string = result      
        i = i + 1
        
    return  result



print cellular_automaton('.x.x.x.x.', 17, 2)
#>>> xxxxxxx..

print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx

