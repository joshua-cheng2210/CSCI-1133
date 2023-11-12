def wordcount(fname):
    try:
        count = 0
        fp = open(fname)
        lines = fp.read()

        words = lines.split()
        fp.close
        return len(words)
    except FileNotFoundError:
        print("Bad File name")
        return -1

# print(wordcount("tet.txt"))

import random
def make_data(fname):
    fpout = open(f"{fname}.csv", "w")
    for i in range(1, 1001):
        fpout.write(f"{str(i)}, {str(random.randint(-1000,1000))}\n")
    fpout.close()
def read_data(fname):
    try:
        fp = open(fname)
        max = int(fp.readline().split(",")[1])
        min = max
        num = max
        for line in fp:
            if(line != ""):
                num = int(line.split(",")[1])
            if num > max:
                max = num
            if num < min:
                min = num
        print(min,max)
    except FileNotFoundError:
        print("Bad File name")
    
# read_data("random_numbers.csv")

import statistics

def find_stats(fname):
    fp = open(fname)
    fp.readline()
    lst = []
    num = float(fp.readline().split(",")[5])
    max = num
    min = num
    sum = num
    count = 1

    for line in fp:
        num = float(line.split(",")[5])

        if num > max:
            max = num
        if num < min:
            min = num
        lst.append(num)
        sum += num
        count += 1
        mean = sum/count
        median = statistics.median(lst)

    print(min, max, mean, median)

find_stats("MDT.csv")
