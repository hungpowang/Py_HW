import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img_path = input("請輸入圖片檔名：")
img = cv2.imread(img_path, 1)

text = input("請輸入浮水印內容：")
px = int(input("請輸入浮水印尺寸(px)："))
fontPath = "/System/Library/Fonts/Menlo.ttc"  # on MacOS
font = ImageFont.truetype(fontPath, px)

# np.array --> PIL image
imgPil = Image.fromarray(img)
# add text
draw = ImageDraw.Draw(imgPil)
draw.text((100, 200),  text, font = font, fill = (202, 202, 202))
img = np.array(imgPil)

cv2.imshow('Watermarked Image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
