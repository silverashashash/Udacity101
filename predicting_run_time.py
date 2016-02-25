import time
def time_execution(code):
	start = time.clock()
	result = eval(code) #evaluate any string as if it's a python command
	run_time = time.clock() - start
	return result, run_time