from PIL import Image


#读取图像
pil_im = Image.open('Penguins.jpg')
#转化成灰色
pil_im_gray = pil_im.convert('L')
print(pil_im_gray)

#保存图片
def saveImage(obj):
    if os.path.exists('test.jpg'):
        os.remove('test.jpg')
    obj.save('test.jpg')
pil_im_gray.save('Penguins_gray.jpg')

#将图片后缀名改为 .jpg
def changeToJPG(infile):
    outfile = os.path.splitext(infile)[0] + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('connot convent',infile)

#返回指定目录中，文件后缀名.jpg的文件
def get_imagelist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

#创建缩列图
pil_im.thumbnail((128,128))
#复制和粘贴图像区域，使用crop方法进行复制，使用paste进行粘贴
box = (100,100,400,400)#四元组进行指定，分别是上，下，左，右
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)

#调整尺寸和旋转
out = pil_im.resize((128,128))
saveImage(out)
#进行旋转
out = pil_im.rotate(45)
saveImage(out)