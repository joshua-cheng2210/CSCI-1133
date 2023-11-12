candidate1 = [95, 93, 50, 91, 98, 90, 82]
candidate2 = [65, 75, 85, 95, 100, 100, 85]
candidate3 = [100, 100, 95, 85, 75, 65, 80]
candidate4 = [98, 70, 55, 61, 98, 90, 90]
candidate5 = [100, 95, 55, 61, 75, 95, 90]
candidate6 = [95, 90, 98, 88, 93, 95, 94]
candidate7 = [90, 80, 80, 100, 70, 75, 90]
candidate8 = [80, 83, 79, 83, 77, 77, 82]
candidate9 = [90, 100, 100, 98, 100, 99, 55]
candidate10 = [77, 82, 92, 100, 95, 92, 70]

def filter_4_high(cand):
    counter = 0
    for i in cand:
        if i >= 85:
            counter += 1
    if counter >= 4:
        return True
    else:
        return False

print(filter_4_high(candidate2)) #Should output True
print(filter_4_high(candidate7)) #Should output False
