# pip3 install Pillow
from PIL import Image

im = Image.open("1.png")
print('宽x高: %d x %d ' % (im.size[0], im.size[1]))
print('图片模式: ' + im.mode)
print('图片格式: ' + im.format + "\n")

new_s = input("请输入新图片的大小(格式为：宽x高): ")

new_size = new_s.split('x')
new_size[0] = int(new_size[0])
new_size[1] = int(new_size[1])

new_img = im.resize((new_size[0], new_size[1]), Image.ANTIALIAS)
new_img.save("new.png")

print("\n图片修改保存成功！新图片路径为：new.png")
img = Image.open('new.png')
print('新图片宽x高: %d x %d ' % (img.size[0], img.size[1]))
print('新图片模式: ' + img.mode)
print('新图片格式: ' + img.format + "\n")