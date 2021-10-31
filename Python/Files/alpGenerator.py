import string

def alpGenerator():
    alp  = list(string.ascii_lowercase)
    for i in alp:
        for j in alp:
            for k in alp:
                yield (i+j+k)
