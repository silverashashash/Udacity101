# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    i = 0
    rec = 0
    list1 = []
    string1 = ""
    while i < len(source):    
        if source[i] not in splitlist:
            string1 = string1 + source[i]
        else:
            if source[i] in splitlist and source[i-1] not in splitlist:
                list1.append(string1)
                string1 = ""
#            if source[i] in splitlist and source[i-1] in splitlist:
        i = i+1
    
    if string1 != "":
        list1.append(string1)
    return list1
       

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']