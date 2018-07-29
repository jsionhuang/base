import math
import numpy as np
#Sigmoid函数
def sigmoid(x):
    return 1.0/(1+math.exp(-x))

#梯度下降函数gradeAscent的实现如下
#dataMAt:特征矩阵列 classLabel:目标列：alpha步长 maxCycless 循环次数
# 梯度下降公司为：W(t+1) = Wt - α(步长)* Xt(转置矩阵) * error(迭代的梯度)
#如果  \W(t+1) - Wt\向量距离小于m（m指收敛条件的阀值）
#error的计算公司为： error = Y (目标列，就是指向量)- Sigimiod(XWt)
#介绍一下转置矩阵  将矩阵的行和列位置对调
#一个训练数据的矩阵的指向量一般是最后一列数据，他的值一般为1或者0
def gradeAscent(dataMat,classLabel,alpha,maxCycless):
    #mat生成一个目标列矩阵,
    dataMatrix = np.mat(dataMat)
    labelMat = np.mat(classLabel).transpose()
    #shape获得特征 n*m
    m,n = np.shape(dataMatrix)
    #s生成权重[1,1,1]
    weights = np.ones((n,1))
    #在指定循环次数里面
    for i in range(maxCycless):
        #Sigmoid(XWt) 代表第t次将模型权重和特征函数成绩带入Sigmoid函数中
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights