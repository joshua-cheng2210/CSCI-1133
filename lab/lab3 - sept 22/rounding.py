# def roundit(float):
#     round_down_int = float // 1
#     if (float >= 0):
#         temp = float - 0.5
#         if (temp < round_down_int):
#             return round_down_int
#         else:
#             return round_down_int + 1
#     else:
#         temp = float + 0.5
#         if (temp > round_down_int):
#             return round_down_int
#         else:
#             return round_down_int

def roundit(float):
    '''
    firstly,
    i want to check if the float argument is negative.
    if it is negative, i want to convert it to positive
    '''
    if (float < 0):
        negative = 1
        float = float * -1
    else:
        negative = 0
    '''
    secondly,
    now that the float variable is positive,
    I will then do the rounding process.

    and store the integer value in the variable, ret_int
    '''
    round_down_int = float // 1
    float = float - 0.5
    if (float < round_down_int):
        ret_int = round_down_int
    else:
        ret_int = round_down_int + 1
    
    '''
    lastly,
    if the float arguement was initially negative,
    I will multiply -1 to the ret_int.

    and then return ret_int
    '''
    if (negative == 1):
        return int(ret_int * -1)
    else:
        return int(ret_int)


print(roundit(1.6))
print(roundit(1.2))
print(roundit(0))
print(roundit(-1.2))
print(roundit(-1.6))
