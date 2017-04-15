# from PIL import Image,ImageFilter
#
# im = Image.open('kora.png')
#
# # w,h  =  im.size
# #
# # print('origin image size: %s x %s' % (w,h))
#
# # im.thumbnail(w // 2,h // 2)
#
# # print('Resize image to: %sx%s' % (w//2, h//2))
#
# # im.save('thumbnail.jpg','jpeg')
#
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.png','png')
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

#random

def rndChar():
    return chr(random.randint(65,90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))



width = 60 * 4
height = 60

image = Image.new('RGB',(width,height),(255,255,255))

#font
font = ImageFont.truetype('Arial.ttf',36)

#draw

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())



#text
for t in range(4):
    draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())

#blur

image = image.filter(ImageFilter.GaussianBlur)

name = random.randint(1, 10000000)

image.save('code%s.png'% name,'png')











