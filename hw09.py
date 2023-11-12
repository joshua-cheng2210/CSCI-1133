import random

def weighted_choice(dic):
    '''
Purpose: a function that does a weighted random selection from the keys of a dictionary, using the values as the weights.
Parameter(s): dict: a dictionary of options as keys and weights as values
Return Value: return a value base on it's weight
'''
    out = []
    for xxx in dic:
        for i in range(dic[xxx]):
            out.append(xxx)
    return random.choice(out)


def count_votes(district, office):
    '''
Purpose:
    creating a dictionary representing the vote counts for a specific office
Parameter(s):
    district should be the name of a file containing all voting data for a given district, in the format specified above.
    office should be the name of one of the column titles present in the CSV file.  You can assume that the office passed in will match one of the columns in the CSV file.  
Return Value:
    return a dictionary in which each key is a name present in the column corresponding to the given office, and the value represents how many times that name occurs within the column.

'''
    out = {}
    f = open(district)
    fp = f.readlines()

    for vote in range(len(fp)):
        fp[vote] = fp[vote].strip().split(",")
    
    i = fp[0].index(office)
    for votes in fp[1:]:
        if votes[i] not in out:
            out[votes[i]] = 1
        else:
            out[votes[i]] += 1
    f.close()
    return out

# def random_sent(source_file, length):
#     f = open(source_file)
#     fp = f.read()
#     fp = fp.split()
#     word_choice = {}
#     out = []

#     for words in fp:
#         if words not in word_choice:
#             word_choice[words] = 1
#         else:
#             word_choice[words] += 1

#     for i in range(length):
#         out.append(weighted_choice(word_choice))
#     out = " ".join(out)

#     f.close()
#     return out

def random_sent(source_file, length):
    '''
Purpose:
    creating a dictionary representing the vote counts for a specific office
Parameter(s):
    source_file is a string representing the name of a file in the current directory, which we’ll use as a basis for producing our text
    length is an integer representing the number of words in our output text
Return Value:
    return a dictionary in which each key is a name present in the column corresponding to the given office, and the value represents how many times that name occurs within the column.
'''
    f = open(source_file)
    fp = f.read()
    fp = fp.split()
    word_choice = {}
    out = []

    for xxx in fp:
        if xxx not in word_choice:
            word_choice[xxx] = 1
        else:
            word_choice[xxx] += 1

    word = weighted_choice(word_choice)
    
    for i in range(length):
        out.append(word)

        next_word_choice = {}
        for yyy in range(len(fp)):
            if fp[yyy] == word:
                try:
                    if fp[yyy + 1] not in next_word_choice:
                        next_word_choice[fp[yyy + 1]] = 1
                    else:
                        next_word_choice[fp[yyy + 1]] += 1
                except:
                    next_word_choice[weighted_choice(word_choice)] = 1
    
        word = weighted_choice(next_word_choice)
    out = " ".join(out)

    f.close()
    return out

