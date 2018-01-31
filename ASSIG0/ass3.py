def numbers(number):
    number=int(number)
    output=[]
    numberlist=[]
    for i in range(1,(number+1)):
        for j in range(1,(i+1)):
            result=i*j
            numberlist.append(result)
        output.append(numberlist)
        numberlist=[]
    print(output)        
    
# number=input('input number')
# print(numbers(number))