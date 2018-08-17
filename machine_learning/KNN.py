import math
import operator
# 1.加载打标好的数据
#2.计算每一个预测对象和所有数据的距离，一般通过求欧式距离实现
#3.欧式距离他能描述n维空间两件之间的距离
#4.在决策集中比较各个类别的数据点的个数，选取个数最多的类别作为预测数据的最终类别
#求两个向量的欧式距离，输入向量1，向量2，和向量的维度
def euclidenDistance(inst1,inst2,length):
    distance = 0
    for x in range(length):
        distance += pow((inst1[x] - inst2[x]),2)
    return math.sqrt(distance)

#在数据集中找到所需要预测数据的的K个最近临近点兵返回  输入  数据集，预测集，以及k值
def getNeighbors(trainingSet,testInstance,k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclidenDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

#返回对目标值的预期值
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),key = operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]


if __name__ == '__main__':
    trainSet = [[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'a'],[1,1,3,'a'],[4,4,4,'b'],[0,0,0,'a'],[4,4.5,4,'b']]
    testInatance = [5,5,5]
    #获得与他最近的几个点
    k = 3
    #获得测试数据最邻近的几个矩阵
    neighbor = getNeighbors(trainSet,testInatance,k)
    reponse = getResponse(neighbor)
    print('Neighbor is:',neighbor)