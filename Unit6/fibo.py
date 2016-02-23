#################solution###############
######faster fibonacci##################
def fibonacci(n):
	current  = 0
	after = 1 
	for i in range(0,n):
		current , after = after, current + after
	return current

#############quiz########################
def fibonacci(n):
    i = 2
    result = [0,0]
    result[0] = 0
    result[1] = 1
    while i <= n:
        result.append(result[i-1]+result[i-2])
        i = i + 1
    return result[n]

##########mathematically####################
def fibonacci(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
