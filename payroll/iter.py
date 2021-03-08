m=0
j=98
i=97
for x in range(5):
	i=j+3
	for y in range(j-1,i):
		print(chr(y),end='')
		m=y
	j=m
	j+=1
	print()
	