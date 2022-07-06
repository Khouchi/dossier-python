def f2(l):
    result=0
    for i in range(len(l)):
        result = result+l[i]
    return result
liste5= [i for i in range(1,513) if i%3 >0 ]
print(f2(liste5))




