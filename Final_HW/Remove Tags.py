# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.
    
def start_tag(string):
    start = 0
    while start < len(string):
        if string[start] == '<':
            return start
        start = start + 1
        
def stop_tag(n, string):
    stop = 0
    while stop < len(string) - n + 1:
        if string[stop] == '>':
            return stop
        stop = stop + 1

def remove_tags(string):
    result = []
    word = ''
    tag = ''
    n = len(string)
    i = 0
    while i < n:
        if string[i] == '<':
            start = start_tag(string[i:])
            stop = stop_tag(start, string[i:])
            word = word + " "
            i = i + stop 
        else:
            word = word + string[i]
        i = i + 1
    result = word
    return result.split()


print remove_tags( 'This <i>line</i> has <em>lots</em> of <b>tags</b>.')

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']


###########solutions###########
def remove_tag(string):
	start = string.find('<')
	while start != -1:
		end = string.find('>', start)
		string = string[start:] + " " + string[end + 1:]
		start = string.find('<')
	return string.split()
	