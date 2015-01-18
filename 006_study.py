import Image

im=Image.open('/home/lxz/python/oxygen.png')
lregion=(0,0,0,0)
for a in range(629):
#	box=(a,33,a+1,34)
	region=im.getpixel((a,43))
	if lregion!=region:
		print chr(region[1]),
		lregion=region
#im.thumbnail((w//2,h//2))
#im.save('/home/grid/python/oxygen.jpg','jpeg')
