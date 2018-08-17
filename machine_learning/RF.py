#随机森林是树状的分类算法，由多个决策树组成
#决策树的特征是抽样生成的，有放回第抽取决策树的m个特征，作为决策树的特征
#每颗树的训练数据也是随机生成的，如果训练集有N个巡礼啊数据，训练模型是就回随机抽取n个样例数据进行训练
#决策树一般用二叉决策树，最终结果有决策树的投票来决定


from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor#黑盒
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()#load_iris()函数拿到开源数据
rf = RandomForestRegressor()
rf.fit(iris.data[:350],iris.target[:350])#RandomForestRegressor的fit函数进行训练，
# fit函数第一个字段是特征列，第二个字段是存储的目标列
instance = iris.data[100]#预测集是 instance，即数据集中第51条数据
print(instance)
#目标
print(iris.target[100])
#区预测，rf已经训练好了
print(rf.predict([instance]))