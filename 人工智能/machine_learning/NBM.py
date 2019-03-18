#朴素贝叶斯分类器
# -*- coding:utf-8 -*-
#from naiveBayesClassifier import tokenizer
#rom naiveBayesClassifier.trainer import Trainer
#from naiveBayesClassifier.classifier import Classifier
#from numpy import *
#1.贝叶斯公司 P(A\B) = P(A)*P(B\A) / P(B)   P(A)先验概率  P(B\A)条件概率
#2.脏话的识别   训练数据（样本数据，样本类别） 词语集 将样本数据数字化（出现在词语集标为1，或者为0）
#3. P(是脏话|m) = P(是脏话)*P(m|是脏话) /P(m)   (求概率时进行拉布拉斯平滑处理)
from numpy import *
import math
# 文本数据集
def loadDataList():
    postingList = [
        ['my','dog','has','flea','problems','help','please'],
        ['maybe','not','take','him','to','dog','park','stupid'],
        ['my','dalmation','is','so','cute','I','love','him'],
        ['stop','posting','stupid','worthless','garbage'],
        ['mr','licks','ate','my','steak','how','to','stop','him'],
        ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0,1,0,1,0,1]
    return postingList ,classVec

 # 提取训练集中的所有词
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet :
        vocabSet = vocabSet | set(document)  # 两个集合的并集
    return list(vocabSet)

# 根据类别对词进行划分数值型的类别
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            print('数值类别',word,)
            returnVec[vocabList.index(word)] = 1
        else :
            print ("the word : %s is not in my Vocabulary!" % word)
    print('returnVec',returnVec)
    return returnVec

# 文档词袋模型，可以对重复的单词计数
def bagOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

'''
求贝叶斯公式中的先验概率 pAbusive ,条件概率 p0Vect、p1Vect；函数中所求的概率值
是变形值，不影响贝叶斯的核心思想：选择具有最高概率的决策
'''
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)  # 样本中对象的个数
    numWords = len(trainMatrix[0]) # 样本中所有词的集合个数
    pAbusive = sum(trainCategory) / float(numTrainDocs) # 对类别只有两种的先验概率计算
    # 对所有词在不同的类别下出现次数的初始化为1，为了防止计算条件概率出现为0
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    # 对不同类别出现次数的初始化为2，词的出现数初始数为1的情况下，增加分母值避免概率值大于1
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):  # 遍历所有对象
        if trainCategory[i] == 1: # 类别类型的判断
            p1Num += trainMatrix[i]  # 对所有词在不同的类别下出现次数的计算
            p1Denom += sum(trainMatrix[i]) # 对不同类别出现次数的计算
        else:
            p0Num += trainMatrix[i] # 对所有词在不同的类别下出现次数的计算
            p0Denom += sum(trainMatrix[i]) # 对不同类别出现次数的计算
    print('条件概率p1：',p1Num / p1Denom)
    print('条件概率p0：',p0Num / p0Denom)
    p1_condition =  p1Num / p1Denom
    p0_condition =  p0Num / p0Denom
    p1Vect = [log(x) for x in p1_condition]  # 条件概率,用对数的形式计算是为避免概率值太小造成下溢出
    p0Vect = [log(x) for x in p0_condition]   # 条件概率,用对数的形式计算是为避免概率值太小造成下溢出
    print('p1Vect:',p1Vect,'p0Vect:',p0Vect)
    return p0Vect, p1Vect, pAbusive

# 计算后验概率，并选择最高概率作为预测类别
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec ) + math.log(pClass1) # 对未知对象的单词的每一项的条件概率相加（对数相加为条件概率的相乘）
    p0 = sum(vec2Classify * p0Vec ) + math.log(1.0-pClass1 ) # 后面加上的一项是先验概率
    print(p1,p0)
    if p1 > p0:
        return 1
    else :
        return 0

 # 对侮辱性语言的测试
def testingNB():
    listOposts, listClasses = loadDataList() # 训练样本的数据，listOposts 为样本，listClasses 为样本的类别
    myVocabList = createVocabList(listOposts ) # 样本的词汇集 ,样本出现的全部词语
    trainMat = [] # 对样本的所有对象相关的单词转化为数值 ，出现了就是1，没出现就是0
    for postinDoc in listOposts :
        trainMat.append(setOfWords2Vec(myVocabList ,postinDoc ) )
    #pAb是先验概率 p0V是每个词语是不是脏话的概率 p1V是指每个词语是脏话的概率
    p0V, p1V, pAb = trainNB0(array(trainMat),array(listClasses)) # 样本的先验概率和条件概率

    testEntry = ['love','my','dalmation','love'] # 未知类别的对象
    thisDoc = array(setOfWords2Vec(myVocabList ,testEntry ) ) # 对未知对象的单词转化为数值
    print(testEntry ,'classified as : ',classifyNB(thisDoc, p0V,p1V,pAb)) # 对未知对象的预测其类别

    testEntry = ['stupid','garbage'] # 未4知类别的对象
    thisDoc = array(setOfWords2Vec(myVocabList ,testEntry )) # 对未知对象的单词转化为数值
    print(testEntry, 'classified as : ', classifyNB(thisDoc, p0V, p1V, pAb)) # 对未知对象的预测其类别

# 邮件文件解析
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\w*', bigString) # 利用正则语言对邮件文本进行解析
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] # 限定单词的字母大于2

# 完整的垃圾邮件测试函数
def spamTest():
    docList=[];classList = []; fullText = []
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' %i ).read())
        docList.append(wordList) # 把解析后的邮件作为训练样本
        fullText.extend(wordList)
        classList.append(1) # 邮件所对应的类别
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)   # 把解析后的邮件作为训练样本
        fullText.extend(wordList )
        classList .append(0) # 邮件所对应的类别
    vocabList = createVocabList(docList) # 样本生成的词汇集
    # 随机产生十个测试样本和四十个训练样本
    trainingSet = range(50);testSet = []
    for i in range(10):
        randIndex = int (random.uniform(0,len(trainingSet )))
        testSet.append(trainingSet [randIndex ])
        del[trainingSet[randIndex]]
    # 对训练样本进行词的转化成数值类型
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet :
        trainMat.append(setOfWords2Vec(vocabList, docList [docIndex ]) )
        trainClasses.append(classList[docIndex ])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses)) # 训练样本的先验概率及条件概率
    errorCount = 0 # 测试样本的出错数初始化
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList ,docList[docIndex ]) # 测试对象的词的数值转化
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex ]: # 预测的类别与真实类别的对比
            errorCount += 1
    print ('the error rate is : ', float (errorCount )/ len(testSet)) # 测试样本的出错率

if __name__ == '__main__':
    #testingNB() # 对侮辱性评价的测试
    spamTest()  # 对垃圾邮件的测试

