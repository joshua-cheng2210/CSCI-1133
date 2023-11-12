
def longest_even(shows):
    '''
    Purpose:
        find out Kai's favourite show
    Parameter(s):
        shows: a list of possible shows
    Return Value:
        return favourite show - longest even show name
    '''
    length = 0
    fav_show = ""
    for show in shows:
        if (len(show) > length and len(show) % 2 == 0):
            fav_show = show
            length = len(show)
    
    return fav_show

# if __name__ == '__main__':
#     print(longest_even(['Dr. Who', 'She-Ra', 'NCIS'])) #'She-Ra'
#     print(longest_even(["a", "abc", "abcde"])) # ""
#     print(longest_even([".", "..", "...", "...."])) # "...."

def prior_to(data, key):
    '''
    Purpose:
        find the hidden info in the list of info
    Parameter(s):
        data: the list of info containing the hidden info
        key: the pattern of the hidden info
    Return Value:
        the hidden info
    '''

    new_list = []
    for xxx in range(len(data)):
        if data[xxx] == key:
            new_list.append(data[xxx - 1])
    return new_list

def all_three(social, grades, sleep):
    '''
    Purpose:
        find the names that appears in all 3 of the list given
    Parameter(s):
        social, grades, sleep - a list of students
    Return Value:
        list of student that appears in all 3 of the list catogory.
    '''
    new_list = []
    for xxx in social:
        if (xxx in grades and xxx in sleep):
            new_list.append(xxx)
    print(new_list)
    return new_list







