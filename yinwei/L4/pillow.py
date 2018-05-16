#Pillow、requests、chardet、psutil、bs4、pandas、numpy、matplotlib

#Pillow 是是一个 Python 图像处理库

#安装
#pip install Pillow
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#操作图像
#图像的缩放
# im = Image.open('img/bird.jpg')
# width,height = im.size #im.size返回一个元组
# im.thumbnail((width//3,height//4))
# im.save('img/thumbnail.jpg','jpeg')

#图片模糊
# from PIL import ImageFilter
# im = Image.open('img/bird.jpg')
# # 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('img/blur.jpg', 'jpeg')

#生成字母验证码
# import random
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
#
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
# # 240 x 60:
#
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('img/scode.jpg', 'jpeg')

#新建图像
# newIm = Image.new('RGB',(100,100),'red')
# newIm.save('img/01.png')

#更多功能请看api
#https://pillow.readthedocs.io/en/latest/handbook/index.html