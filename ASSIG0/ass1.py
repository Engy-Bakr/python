def vowelsremover(word):
        vowels = ('a', 'e', 'i', 'o', 'u')

        for i in word:
                if i in vowels:
                        word=word.replace(i,'')        
        return(word)



# word=input('input the word ')
# print(vowelsremover(word))