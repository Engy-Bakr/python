def calcarea(shape,p1,*p2):
    if (shape=='t'):
        for i in p2:
            area=(0.5*p1*i)
    if (shape=='r'):
        if len(p2) != 0:
            for i in p2:
                area=p1*i
        else:
            area=p1*p1
    if (shape=='c'):
        area=3.14*p1**2
    return area

# shape=input('input the shape')
# p1=int(input('input the first parameter'))
# p2=(input('input the second parameter if exist'))
# if p2:
#     p2=int(p2)

# print(calcarea(shape,p1,p2))

# print(calcarea('t',5,6))
# print(calcarea('c',5))
# print(calcarea('r',5))
# print(calcarea('r',6,10))