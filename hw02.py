import math

#TODO: Fill out the Purpose, Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

# Example functions for background reading

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have
    Return Value:
        The amount in cents we have
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle
    Return Value:
        The given angle's measure in radians
    '''
    radians = deg * math.pi / 180
    return radians




# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        to convery the temperature in celcius to fahrenheit
    Parameter(s):
        temperature in celcius
    Return Value:
        temperature in fahrenheit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose:
        print 5 lines with 5 stars each line
    Parameter(s):
        None
    Return Value:
        None
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    

# Part B: Write out a few simple conversions

def circumference_circle(radius):
    """
    Purpose:
        returns the circumference of the circle
    Parameter(s):
        radius is half the length of the diameter of the circle
    Return Value:
        the circumference of the circle
    """
    return 2 * math.pi * radius

def gallons_to_liters(gallons):
    """
    Purpose:
        converts number of gallons into number of liters
    Parameter(s):
        number of gallons
    Return Value:
        returns the number of gallons in terms of liters
    """
    return gallons * 3.78541
    
def days_to_minutes(days):
    """
    Purpose:
        provides the number of minutes inside the number of days input
    Parameter(s):
        number of days
    Return Value:
        return the number of minutes in the number of days input
    """
    return days * 24 * 60



# Part C: Calculate cost of an ice skating field trip

def trip_cost(students, teachers, own_skates):
    """
    Purpose:
        calculates the total cost of the trip
    Parameter(s):
        param1: number of students going for the trip
        param2: number of teachers going for the trip
        param3: number of students bringing their own own_skates
    Return Value:
        returns the total cost of the trip
    """
    
    num_ppl = students + teachers
    bus_cost = math.ceil(num_ppl / 50) * 200
    lunch_cost = students * 5 + teachers * 7
    rental_cost = (students - own_skates) * 4

    print("Bus cost:", bus_cost)
    print("Lunch cost: ", lunch_cost)
    print("Rental cost: ", rental_cost)

    return (bus_cost + lunch_cost + rental_cost)
