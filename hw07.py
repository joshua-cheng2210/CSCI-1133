def starting_string(str_one, str_two):
    '''
Purpose:
    a function starting_string(str_one, str_two) that takes in two strings, and returns the common substring that begins each string
Parameter(s):
    str_one and str_two -> the 2 strings to compare
Return Value: 
    returns the common substring that begins each string
'''
    out = ""
    index = 0
    max_index = min([len(str_one), len(str_two)]) - 1
    while(index <= max_index and str_one[index] == str_two[index]):
        out += str_one[index]
        index += 1
    return out

if __name__ == '__main__':
    print(starting_string('Episode II: Attack of the Clones', 'Episode III: Revenge of the Sith')) #Episode II
    print(starting_string('abc', 'abc')) #abc
    print(starting_string('abc', 'def')) #

def find_substring(str, substr):
    '''
Purpose:
    find all the index where substr appear in str
Parameter(s):
    needle in the haystack; str = haystack, substr = needle
Return Value:
    return a list of all the locations where the substr is found in str
'''
    out = []
    index = 0
    while (index <= (len(str) - len(substr))):
        if starting_string(str[index:], substr) == substr:
            out.append(index)
        index += 1
    return out

def build_csv_string(data):
    '''
Purpose:
    convert the list data into a csv string
Parameter(s):
    a list data. data will be a list of lists, where each sub list is of length 1, 2, or 3.  
    Length 1 lists will contain a name (as a string). 
    Length 2 lists will contain a name and an assignment title (as a string). 
    Length 3 lists will contain a name, an assignment title, and a score (as a float or int).  
Return Value: 
    a valid csv string where each sublist is a record in the string. 
'''
    out = "name,assignment,grade\n"
    for names in range(len(data)):
        out += f"{data[names][0]},"
        try:
            out += f"{data[names][1]},"
        except:
            out += f"N/A,"
        try:
            out += f"{data[names][2]}"
        except:
            out += f"0"
        if names != (len(data) - 1):
            out += f"\n"
    return out