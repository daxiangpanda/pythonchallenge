c=[[1]]
for i in range(30):
	pos=0
	temp=c[i]
	length=len(temp)       
	new=[]
	while pos<length:
		count=1
		while pos+1<length and temp[pos]==temp[pos+1]:
			count+=1
			pos+=1
		new.append(count)
		new.append(temp[pos])
		print new 
	c.append(new)
	pos+=1
print length(c)
