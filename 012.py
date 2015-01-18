#open file evil2.gfx first,then read it.create 5 files,then split the file into 5 files
f=open('evil2.gfx','r')
str=f.read()
a=['a','b','c','d','e']
b=0
for i in range(5):
	a[i]=open('%d'%i,'w')
	for j in range(len(str)):
		if j%5==b:
			a[i].write(str[j])
	b=b+1	
	a[i].close()	


