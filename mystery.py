def f1(l):
	result=0
	for i in range(len(l)):
		if l[i]%2 == 0:
			result += l[i]
	return result
	
def f2(l):
	result=0
	for i in range(len(l)):
		if i%2 == 0:
			result += l[i]
	return result
	
liste = [0,1,2,3,4,5,6,7,8,9,10]
print('Avec f1 :',f1(liste))
print('Avec f2 :',f2(liste))