def sum_odd_digits(a_number):
    '''
    Purpose:
        sum all the odd digit in the number
    Parameter(s):
        a_number: a positive integer
    Return Value:
        the sum of all of the odd digits which make up the given number
    '''
    sum = 0
    while (a_number != 0):
        if ((a_number % 10) % 2 == 1):
            sum = sum + (a_number % 10)
        a_number = a_number // 10
    return sum

def next_divisor(n, lower_bound):
    '''
    Purpose:
        finding the divisor of a number if there is
    Parameter(s):
        n: the number you will search for a divisor of
        lower_bound: an integer, lesser than the divisor if there is
    Return Value:
        the smallest divisor which is greater than lower_bound
    '''
    while(lower_bound <= n):
        lower_bound += 1
        if (n % lower_bound == 0):
            return lower_bound
    else:
        return (-1)

def play_nim(winning_number):
    '''
    Purpose:
        a game
    Parameter(s):
        winning_number: the number both player will try to reach
    Return Value:
        the winning player
    '''
    print(f"The goal is {winning_number}. Pick a number between 1 and 3")
    rounds = 1
    current_score = 0
    while (current_score < winning_number):
        if (rounds % 2 == 1):
            x = int(input(f"Current Score {current_score}. Player 1 enter a number: "))
        else:
            x = int(input(f"Current Score {current_score}. Player 2 enter a number: "))
        while (x < 1 or x > 3):
            print("Invalid number, try again.")
            if (rounds % 2 == 1):
                x = int(input(f"Current Score {current_score}. Player 1 enter a number: "))
            else:
                x = int(input(f"Current Score {current_score}. Player 2 enter a number: "))
        if (x >= 1 and x <= 3):
            current_score = current_score + x
        if (current_score >= winning_number):
            if (rounds % 2 == 1):
                return 1
            else:
                return 2
        rounds += 1
