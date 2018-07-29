from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.model_selection import train_test_split
import scipy,numpy as np
from sklearn import neighbors

#trian_test_split方法测试
'''
将矩阵随机划分为训练子集和测试子集，并返回划分好的训练集测试集样本和训练集测试集标签
train_data：被划分的样本特征集
train_target：被划分的样本标签
test_size：如果是浮点数，在0-1之间，表示样本占比；如果是整数的话就是样本的数量
random_state：是随机数的种子。
随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。
随机数的产生取决于种子，随机数和种子之间的关系遵从以下两个规则：
种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。
'''
X, y = np.arange(10).reshape((5, 2)), range(5)
print(X,list(y))
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)
print('X_train',X_train)
print('y_train',y_train)
print('X_test',X_test)
print('y_test',y_test)
#高斯朴素贝叶斯
iris = datasets.load_iris()
X_trian,X_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.4,random_state=0)
clf = GaussianNB()
clf.fit(X_trian,y_train)
print(clf.score(X_test,y_test))

#KNN
clf = neighbors.KNeighborsClassifier()
clf.fit(X_trian,y_train)
print(clf.score(X_test,y_test))




