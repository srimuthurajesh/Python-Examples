from PIL import Image

img = Image.open('noSystemIsSafe.jpg')
print(img.size)
print(img.format)
img.show()

#crop image
area = (100,100,300,375)	#in px(startPoint x-axis,startPoint y-axis,endPoint x-axis,endPoint x-axis)	
img.crop(area).show();

#resize image
img.resize((250,250)).show()

#showing only Red alone and Green alone and Blue alone
r,g,b = img.split()		#gives list of rgb channel 
r.show()
g.show()
b.show()

#merge images by channels
img2 = Image.open('smile.jpg')
r2,g2,b2 = img2.split()
Image.merge('RGB',(r2,g1,b1)).show()

#flip image
img.transpose(Image.FLIP_LEFT_RIGHT).show()
img.transpose(Image.ROTATE_90).show()

#image filters
img.convert("L").show()		#L for luminous B/W

#Blur image
import PIL import ImageFilter
img.filter(ImageFilter.BLUR).show()		#shows blur image
img.filter(ImageFilter.DETAILS).show()
img.filter(ImageFilter.FIND_EDGES).show()	#image will become sharp	




