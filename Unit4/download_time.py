# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
def output(number, unit):
    return "{0} {1}{2}".format(number, unit, "s" if number != 1 else "")


    
def convert_seconds(second):
    hour = 0
    minu = 0
    if second/60 >=60:
        hour = (second/60 )/60
        minu = (second/60 )%60
    else:
        hour = 0
        minu = second/60 
    sec = second - (int(minu)*60+int(hour)*3600)
    return  "{0}, {1}, {2}".format(output(int(hour), "hour"), output(int(minu), "minute"),
                                  output(sec, "second"))    

def convert_unit(size, unit):
    if unit[1] == 'B':
        size = size*8.
    if unit[0] == 'M':
        size = size * 2**10    
    if unit[0] == 'G':
        size = size * 2**20
    if unit[0] == 'T':
        size = size * 2**30
    
    return size
        

def download_time(file_size, file_unit, bandwidth, bandwidth_unit):
    second = 0
    file_size= convert_unit(file_size, file_unit)
    bandwidth = convert_unit(bandwidth, bandwidth_unit)
    
    second = file_size/bandwidth
    return convert_seconds(second)
    



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')



