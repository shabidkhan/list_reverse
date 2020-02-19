def rev(n):
	for i in range(len(n)//2):
		n[i],n[len(n)-(i+1)]=n[len(n)-(i+1)],n[i]
	return n
a=[1,23,4,5,6,7,8,3]

print (rev(a))
