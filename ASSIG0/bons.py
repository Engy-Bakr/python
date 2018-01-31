def vowelsremover(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    newlist=[]
    for j in strlist:
        word=j
        for i in j:
            if i in vowels:
                word=word.replace(i,'') 
        newlist.append(word)   
    return newlist

# strlist=['sara','ali']
# print(vowelsremover(strlist))