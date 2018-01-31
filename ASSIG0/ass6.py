def mario(number):
    number=int(number)
    for i in range(1,number+1):
        print(" "*(number-i)+'*'*i)

number=input('input the number')
mario(number)
