# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
  

def get_row(p,n):
    return p[n]

def get_coloum(p,n):
    m = len(p)
    q = []
    while m>0:        
        k = p[m-1]
        q.append(k[n])
        m = m-1 
    return q

def test_if(a_set):
    n = len(a_set)
    i = 1
    while i <= n:
        if not i in a_set:
            return False
        i = i+1
    return True
        
def check_sudoku(a_list_numbers):
    n = len(a_list_numbers)
    i = 1
    result = True
    while i < n:
        result = result and (test_if(get_row(a_list_numbers,i-1)) and test_if(get_coloum(a_list_numbers,i-1)))         
        i = i+1
    return result


'''
def test_rows(a_list):
    n = len(a_list)
    i = 1
    while i<=n:
        j = 1
        while j<=n:
            if not j in get_row(a_list,i-1):
                return False
            j=j+1
        i=i+1
    return True

def test_coloums(a_list):
    n = len(a_list)
    i = 1
    while i<=n:
        j = 1
        while j<=n:
            if not j in get_coloum(a_list,i-1):
                return False
            j=j+1
        i=i+1
    return True




def check_sudoku(a_list_numbers):
    
    return test_rows(a_list_numbers)  and  test_coloums(a_list_numbers)
'''

print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False



