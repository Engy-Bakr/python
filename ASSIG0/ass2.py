def findelem(word,litter):
    output=[]
    for i,j in enumerate(word):
        if litter == j:
            output.append(i)
    return output

# word=input('input the word ')
# litter=input('input the litter ')
# print(findelem(word,litter))