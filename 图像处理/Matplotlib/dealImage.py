from pylab import *
from PIL import Image
import os
from static.config import getImagesDir


#读取图像到数组
im = array(Image.open(os.path.join(getImagesDir(),'test.jpg')))
#绘制图像
imshow(im)
#一些点
x = [100,100,400,400]
y = [200,500,200,500]
#使用红色星状标记绘制点
#plot(x,y)
plot(x,y,'r*')
#plot(x,y,'go-')
#绘制连接前两个点的线,默认是蓝色实现
plot(x[:2],y[:2])

#添加标题，显示绘制的图像
title("Plotting:test.jpg")
#交互式标注,点击图像三次
x = ginput(3)
show()
'''
颜色：蓝色('b') 绿色('g') 红色('h') 青色('c') 品红('m') 黄色('y') 黑色('k') 白色('w')
线型： 实线('-') 虚线('--') 点线(':')
标记: 点(.) 圆圈(o) 正方形(s) 星型(*) 加号(+) 叉号(x)
'''
#图像的轮廓和直方图

#读取图像
im2 = array(Image.open(os.path.join(getImagesDir(),'Penguins.jpg')).convert('L'))
#新建一个图像
figure()
#不适用颜色
gray()
#在原点的左上角显示轮廓图像
contour(im2,origin='image')
axis('equal')
axis('off')

figure()
hist(im2.flatten(),128)
show()


