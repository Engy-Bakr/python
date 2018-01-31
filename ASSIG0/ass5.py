def dic(namelist):
    newdic={}
    for i in namelist:
        if i[0] in newdic:
            newdic[i[0]].append(i)
        else:
            newdic[i[0]]=[i]
    return newdic

# print(dic(['ahmed','mohamed','fatma','ali']))