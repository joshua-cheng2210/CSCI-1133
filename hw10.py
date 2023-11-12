def loop_sum_digits(string):
    '''
Purpose: 
    sum of all the digits in the string using loops
Parameter(s):
    string: a string with both characters and digits
Return Value:
    sum of all the digits in the string
'''

    total = 0
    for x in string:
        try:
            total += int(x)
        except:
            total += 0
    return total

def rec_sum_digits(string):
    '''
Purpose: 
    sum of all the digits in the string using recursion
Parameter(s):
    string: a string with both characters and digits
Return Value:
    sum of all the digits in the string
'''
    if string == "":
        return 0
    elif(string[0].isdigit() == True):
        return int(string[0]) + rec_sum_digits(string[1:])
    else:
        return rec_sum_digits(string[1:])

def collatz(num):
    '''
Purpose:
    Collatz conjecture 
Parameter(s):
    num: a positive number
Return Value:
    a recursive function that returns the list of numbers in the collatz sequence from n to 1, inclusive
'''
    if num == 1:
        return [int(num)]
    else:
        if (num % 2 == 0):
            return [int(num)] + collatz(num / 2)
            # return [num / 2] + [collatz(num / 2)]
        else:
            return [int(num)] + collatz((num * 3) + 1)
            # return [(num * 3) + 1] + [collatz((num * 3) + 1)]

def collect_words(val):
    '''
Purpose:
    combine only the strings together into a list
Parameter(s):
    collection will be of type str, int, float, list, or tuple
Return Value:
    a list of all of the strings contained within the collection.
'''
    if type(val) == int or type(val) == float or val == () or val == []:
        return []
    elif type(val) != int or val != () or val != []:
        if type(val) == str:
            return [val]
        elif type(val) == list:
            # print(val[0], val[1:])
            return collect_words(val[0]) + collect_words(val[1:])
        elif type(val) == tuple:
            return collect_words(val[0]) + collect_words(val[1:])
