import Image
img=Image.open("11.jpg",'r')
width=img.size[0]
height=img.size[1]
even=Image.new(img.mode,(width/2,height/2))
odd=Image.new(img.mode,(width/2,height/2))
for x in range(width):
	for y in range(height):
		pixel=img.getpixel((x,y))
		if x%2==0 and y%2==0:
			odd.putpixel((x/2,y/2),pixel)
		elif x%2==1 and y%2==0:
			even.putpixel(((x-1)/2,y/2),pixel)
		elif x%2==0 and y%2==1:
			even.putpixel((x/2,(y-1)/2),pixel)
		elif x%2==1 and y%2==1:
			even.putpixel(((x-1)/2,(y-1)/2),pixel)
even.save("11_even.jpg")
odd.save("11_odd.jpg")
