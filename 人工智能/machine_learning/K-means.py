#是一种半监督的机器学习方法，是一种聚类算法
#设置k值，k是几，该数据最终就会被分成几类
#初始化数据簇中心点，随机生成初始数据粗
#有了初始质心，算法进行第一次遍历，选出离自己最近的两类数据，第一次是二分
#已经分成两类，开始迭代 ，新的两个质心就是上次被分成两个区域的中心
#然后重复迭代

import numpy as np
import math
def Kmeans(dataSet,k):#dataSet是numpy矩阵，k是质心数量
    m = np.shape(dataSet)[0]
    n = np.shape(dataSet)[1]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroisd = np.mat(np.zeros((k,n)))#质心点
    for index in range(k):
        centroisd[:,index] = np.mat(5+5*np.random.rand(k,1))#random.rand生成随机矩阵格式数据，做为初始质心
    clusterChanged = True
    while clusterChanged:#判断是否聚类结束
        clusterChanged = False
        for i in range(m):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                vecA = np.array(centroisd)[j,:]
                vecB = np.array(dataSet)[i,:]
                distJI = math.sqrt(sum(pow(vecA - vecB,2)))#欧式距离求距离

                if distJI < minDist:
                    minDist = distJI;minIndex = j

            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(np.array(clusterChanged)[:,0] == cent)[0][0]]
            centroisd[cent,:] = np.mean(ptsInClust,axis=0)

    id = np.nonzero(np.array(clusterAssment)[:,0] == cent)[0]
    return centroisd,clusterAssment,id