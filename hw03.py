def bagel_costs(num_bagels, delivery):
    '''
    Purpose: 
        calculate the total cost of the bagel order + delivery cost if needed
    Parameter(s):
        num_bagels - an integer representing how many bagels the customer is purchasing.
        delivery - a boolean value that is True if the customer is paying the extra for delivery, and False if the customer is not.
    Return Value: 
        the total cost in cents of the customer 's order as an integer.
    '''
    price = 0
    if num_bagels <= 6 and num_bagels >= 0:
        price = price + num_bagels * 90
    elif num_bagels >= 7 and num_bagels <= 12:
        price = price + num_bagels * 80
    elif num_bagels >= 13:
        price = price + num_bagels * 70
    if delivery == True:
        price = price + 500
    else:
        price = price
    return price

if __name__ == '__main__':
    print(bagel_costs(9, True)) # Should output 1220
    print(bagel_costs(1, False))
    print(bagel_costs(13, True))

def three_options(test, optionA, optionB, optionC):
    '''
    Purpose:
        print out the prompt, and then print out the options. Next, use the input() function to prompt the user to choose A, B, or C.
    Parameter(s):
        text - a string representing a prompt in a text adventure game
        optionA, optionB, and optionC - strings representing the three possible options
    Return Value:
        return the user’s choice: 'A', 'B', or 'C'. anything other than the input, function will print a statement and return "C"
    '''
    print(f"{test}\n")
    print(f"A. {optionA}")
    print(f"B. {optionB}")
    print(f"C. {optionC}")
    responce = str(input("Choose A, B or C: "))
    print(f"\'{responce}\'")
    if (responce == "A" or responce == "B" or responce == "C"):
        return responce
    else: 
        print("Invalid option, defaulting to C")
        responce = "C"
        return responce

def adventure():
    '''
    Purpose:
        text adventure game
    Return Value:
        the ending of the game: True for a Good ending; otherwise, False
    '''

    question1 = three_options("question1", "Bad", "Bad", "Good")
    if (question1 == "C"):
        return True
    elif (question1 == "B"):
        question2 = three_options("you chose B for question 1", "Good", "Bad", "Bad")
        if (question2 == "A"):
            return True
        else:
            return False
    else:
        question3 = three_options("you chose A for question 1", "Bad", "Bad", "Good")
        if (question3 == "A" or question3 == "B"):
            return False
        else:
            question4 = three_options("you chose C for question 2", "Bad", "Good", "Bad")
            if (question4 == "B"):
                return True
            elif (question4 == "C"):
                return False
            else:
                question5 = three_options("you choose A for question 3", "Good", "Bad", "Bad")
                if (question5 == "A"):
                    return True
                else:
                    return False