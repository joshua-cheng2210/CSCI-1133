def new_cases(date, state):
    '''
Purpose:
    find the amount of new cases
Parameter(s):
    date - data of new cases
    state - abbrievation of the place of the new cases
Return Value:
    returns an integer representing the number of new cases reported by the given state on that date
'''
    f = open("covid_data.csv")
    fp =  f.readline()
    while (fp):
        lst = fp.split(",")
        if (lst[0] == str(date) and lst[1] == str(state)):
            return int(lst[5])
        fp = f.readline()
    f.close()
    return -1

def length_correct(fname, length):
    '''
Purpose:
    produce a new file “mod-<fname>” (where <fname> is replaced by the value of fname). This new file should contain the same content of “fname” but modified.
Parameter(s):
    fname - a name of a file stored as a string
    length - the max length of any line in the file
Return Value:
    None
'''
    # f = open(fname)
    # f_out = open(f"mod-{fname}", "w")
    # fp = f.read()
    # while(fp):
    #     str = fp
    #     while(str):
    #         if (len(str) > (length - 1)):
    #             f_out.write(f"{str[0:length - 1]}\n")
    #             str = str[(length - 1):]
    #         else:
    #             x = str.find("\n")
    #             f_out.write(f"{str[:x]}")
    #             str = str[:x]          
    # f.close()
    # f_out.close()
    # return None

    f = open(fname)
    f_out = open(f"mod-{fname}", "w")
    fp = f.readline()
    while(fp):
        str = fp
        str2 = ""
        x = 1
        for char in str:
            if char != "\n":
                str2 += char
            if x % (length - 1) == 0:
                str2 += "\n"
            x += 1
        f_out.write(str2)
        fp = f.readline()
        if fp:
            f_out.write("\n")
    f.close()
    f_out.close()
    return None

length_correct("test1.txt", 20)

def stretch_model(fname_in, fname_out):
    '''
Purpose:
    transform the vertices to stretch the model by a factor of 2 along the y-axis, and then save the transformed vertices and faces to a file specified by the string fname_out
Parameter(s):
    fname_in - name of file inputed
    fname)out - name of file outputed
Return Value:
'''
    try:
        f = open(fname_in)
    except FileNotFoundError:
        return -1
    f_out = open(fname_out, "w")
    fp = f.readline()
    counter = 0
    while(fp):
        xxx = fp
        xxx = xxx.split(" ")
        if (xxx[0] == "v"):
            xxx[2] = str(float(xxx[2]) * 2)
            ddd = " ".join(xxx)
            f_out.write(ddd)
            counter += 1
        else:
            f_out.write(fp)
        fp = f.readline()
    f.close()
    f_out.close()
    return counter
