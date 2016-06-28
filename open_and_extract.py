import sys
#######################################
#
#   Extracts segment information from
#   Praat TextGrids
#
#
#
#
#######################################

def extract_xmin_xmax(file_name):
    f = open(file_name, 'r')

    found_vowel = False
    found_interval = False
    for x in range(0,1000) :
        target = f.readline()
        if target.endswith("item [4]:\n"):
            found_vowel = True
            break
    if found_vowel != True:
        f.close()
        return
    for x in range(0,1000):
        target = f.readline()
        if target.endswith("intervals [2]:\n"):
            found_interval = True
            break
    if found_interval != True:
        f.close()
        return
    x1 = f.readline()
    x2 = f.readline()
    x1 = float(x1[19:])
    x2 = float(x2[19:])

    f.close()

    return {'xmin':x1,'xmax':x2}

def extract_period(file_name):
    f = open(file_name, 'r')
    found_vowel = False
    found_interval = False
    for x in range(0,1000) :
        target = f.readline()
        if target.endswith("item [5]:\n"):
            found_vowel = True
            break
    if found_vowel != True:
        f.close()
        return
    for x in range(0,1000):
        target = f.readline()
        if target.endswith("intervals [2]:\n"):
            found_interval = True
            break
    if found_interval != True:
        f.close()
        return
    x1 = f.readline()
    x2 = f.readline()
    x1 = float(x1[19:])
    x2 = float(x2[19:])


    f.close()

    return x2-x1