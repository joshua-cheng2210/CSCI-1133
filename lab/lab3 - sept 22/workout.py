def print_letters(val):
    if (val == 1) or (val == 2) or (val == 6):
        print(3)
    elif (val == 3) or (val == 7) or (val == 8):
        print(5)
    else:
        print(4)

def return_letters(val):
    if (val == 1) or (val == 2) or (val == 6):
        return (3)
    elif (val == 3) or (val == 7) or (val == 8):
        return (5)
    else:
        return (4)


def most_letters(x, y, z):
    if (return_letters(x) == return_letters(y)):
        if (return_letters(x) == return_letters(z)):
                return ("Tie!")
        else:
            if (return_letters(x) > return_letters(z)):
                return x
            else:
                return z
    else:
        if(return_letters(x) > return_letters(y)):
            if (return_letters(x) == return_letters(z)):
                return ("Tie!")
            else:
                if (return_letters(x) > return_letters(z)):
                    return x
                else:
                    return z
        else:
            if (return_letters(y) == return_letters(z)):
                return ("Tie!")
            else:
                if (return_letters(y) > return_letters(z)):
                    return y
                else:
                    return z

print(most_letters(9, 8, 5))
print(most_letters(5, 1, 2))
print(most_letters(7, 6, 3))