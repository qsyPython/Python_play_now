
#将裁剪出来的image进行颜色图像识别

import colorsys
import PIL.Image as Image

def get_dominant_color(image):

    #生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))

    max_score = 0

    dominant_color = None

    for count, (r, g, b,a) in image.getcolors(image.size[0] * image.size[1]):

        #跳过纯黑色
        if a == 0:
            continue

        # 将图片颜色转为hsv，
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]

        # 使用cv2.inRange()函数进行背景颜色过滤
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)

        y = (y - 16.0) / (235 - 16)

        # 忽略高亮色
        if y > 0.9:
            continue

        score = (saturation + 0.1) * count

        if score > max_score:

            max_score = score

            dominant_color = (r, g, b)

    return dominant_color

