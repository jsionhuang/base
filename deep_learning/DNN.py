#概念：DNN反之多层次的神经网络，隐藏层互相连接
#个性推荐模型
'''
1）协同过滤：
    （1）基于user的协同过滤：根据历史日志中用户年龄，性别，行为，偏好等特征计算user之间的相似度，根据相似user对item的评分推荐item。缺点：新用户冷启动问题和数据稀疏不能找到置信的相似用户进行推荐。
    (2）基于item的协同过滤：根据item维度的特征计算item之间的相似度，推荐user偏好item相似的item。
    （3）基于社交网络：根据user社交网络亲密关系，推荐亲密的user偏好的item。
    4）基于模型：LR模型，user和item等维度特征输入给模型训练，label是show：clk，根据预估的pctr进行推荐。DNN模型：见下面。
2）基于内容的过滤：抽取item的有意义描述特征，推荐user偏好item相似度高的item，个人觉得像基于item的过滤。
3）组合推荐：根据具体问题，组合其它几种技术进行推荐。
'''
import pandas as pd
import numpy as np
import tensorflow as tf
import os
from static.config  import getFileDir as basefile

file_ratings = basefile() + '/ml-latest-small/ratings.csv'
#1.1导入 用户对电影的评分 表
ratings_df = pd.read_csv(file_ratings)
ratings_df.tail()#tail命令用于输入文件中的尾部内容。tail命令默认在屏幕上显示指定文件的末尾5行。
#1.2.导入电影文件
file_movies = basefile() + '/ml-latest-small/movies.csv'
movies_df = pd.read_csv(file_movies)
print(movies_df.tail())
#1.3将movies_df中的movieId替换为行号
movies_df['movieRow'] = movies_df.index#生成一列‘movieRow’，等于索引值index
print(movies_df.tail())
#2.1 筛选movies_df 的特征
movies_df = movies_df[['movieRow','movieId','title']]
#筛选三列出来
if os.path.exists(basefile() + '/ml-latest-small/moviesProcessed.csv'):
    os.remove(basefile() + '/ml-latest-small/moviesProcessed.csv')
movies_df.to_csv(basefile() + '/ml-latest-small/moviesProcessed.csv', index=False, header=True, encoding='utf-8')
#生成一个新的文件moviesProcessed.csv
print(movies_df.tail())
#2.2 根据moviesId合并 ratings_df 和 movies_df
ratings_df = pd.merge(ratings_df, movies_df, on='movieId')
print(ratings_df.head())
#2.3 筛选ratings_df的特征
ratings_df = ratings_df[['userId','movieRow','rating']]
#筛选出三列
if os.path.exists(basefile() + '/ml-latest-small/ratingsProcessed.csv'):
    os.remove(basefile() + '/ml-latest-small/ratingsProcessed.csv')
ratings_df.to_csv(basefile() + '/ml-latest-small/ratingsProcessed.csv', index=False, header=True, encoding='utf-8')
#导出一个新的文件ratingsProcessed.csv
ratings_df.head()

#3.1 创建电影评分矩阵rating 和评分记录矩阵
userNo = ratings_df['userId'].max() + 1#userNo的最大值
movieNo = ratings_df['movieRow'].max() + 1#movieNo的最大值
#创建电影评分矩阵rating
rating = np.zeros((movieNo,userNo))#创建一个值都是0的数据
flag = 0
ratings_df_length = np.shape(ratings_df)[0]#查看矩阵ratings_df的第一维度是多少
for index,row in ratings_df.iterrows():#interrows（），对表格ratings_df进行遍历
    rating[int(row['movieRow']),int(row['userId'])] = row['rating']#将ratings_df表里的'movieRow'和'userId'列，填上row的‘评分’
    flag += 1
#创建电影评分记录矩阵record
record = rating > 0
print('初始化的评分记录表如下：',record)
record = np.array(record, dtype = int)
print('评分记录表如下：',record)#更改数据类型，0表示用户没有对电影评分，1表示用户已经对电影评分

#3.2构建模型 传入电影评分表和评分记录表
def normalizeRatings(rating, record):
    m, n =rating.shape
    #m代表电影数量，n代表用户数量
    rating_mean = np.zeros((m,1))
    #每部电影的平均得分
    rating_norm = np.zeros((m,n))
    #处理过的评分
    for i in range(m):
        idx = record[i,:] !=0
        #每部电影的评分，[i，:]表示每一行的所有列
        rating_mean[i] = np.mean(rating[i,idx])
        #第i行，评过份idx的用户的平均得分；
        #np.mean() 对所有元素求均值
        rating_norm[i,idx] -= rating_mean[i]
        #rating_norm = 原始得分-平均得分
    return rating_norm, rating_mean

#获得每部电影的评分 和 原始评分-平均得分
rating_norm, rating_mean = normalizeRatings(rating, record)
rating_norm =np.nan_to_num(rating_norm)
#对值为NaNN进行处理，改成数值0
print('处理后的每部电影的评分',rating_norm)
rating_mean =np.nan_to_num(rating_mean)
#对值为NaNN进行处理，改成数值0
print('处理后的每部电影的原始评分减去平均得分',rating_mean)

#3.3开始构建
num_features = 10
X_parameters = tf.Variable(tf.random_normal([movieNo, num_features],stddev = 0.35))
Theta_parameters = tf.Variable(tf.random_normal([userNo, num_features],stddev = 0.35))
#tf.Variables()初始化变量
#tf.random_normal()函数用于从服从指定正太分布的数值中取出指定个数的值，
# mean: 正态分布的均值。stddev: 正态分布的标准差。dtype: 输出的类型

loss = 1/2 * tf.reduce_sum(((tf.matmul(X_parameters, Theta_parameters, transpose_b = True) - rating_norm) * record) ** 2) + 1/2 * (tf.reduce_sum(X_parameters ** 2) + tf.reduce_sum(Theta_parameters ** 2))
#基于内容的推荐算法模型
# 函数解释：
# reduce_sum() 就是求和，reduce_sum( input_tensor, axis=None,  keep_dims=False, name=None, reduction_indices=None)
# reduce_sum() 参数解释：
# 1) input_tensor：输入的张量。
# 2) axis：沿着哪个维度求和。对于二维的input_tensor张量，0表示按列求和，1表示按行求和，[0, 1]表示先按列求和再按行求和。
# 3) keep_dims：默认值为Flase，表示默认要降维。若设为True，则不降维。
# 4) name：名字。
# 5) reduction_indices：默认值是None，即把input_tensor降到 0维，也就是一个数。对于2维input_tensor，reduction_indices=0时，按列；reduction_indices=1时，按行。
# 6) 注意，reduction_indices与axis不能同时设置。

# tf.matmul（a,b）,将矩阵 a 乘以矩阵 b，生成a * b
# tf.matmul（a,b）参数解释：
# 1) a：类型为 float16，float32，float64，int32，complex64，complex128 和 rank > 1的张量。
# 2) b：与 a 具有相同类型和 rank。
# 3) transpose_a：如果 True，a 在乘法之前转置。
# 4) transpose_b：如果 True，b 在乘法之前转置。
# 5) adjoint_a：如果 True，a 在乘法之前共轭和转置。
# 6) adjoint_b：如果 True，b 在乘法之前共轭和转置。
# 7) a_is_sparse：如果 True，a 被视为稀疏矩阵。
# 8) b_is_sparse：如果 True，b 被视为稀疏矩阵。
# 9) name：操作名称（可选）
optimizer = tf.train.AdamOptimizer(1e-4)
# https://blog.csdn.net/lenbow/article/details/52218551
train = optimizer.minimize(loss)
# Optimizer.minimize对一个损失变量基本上做两件事
# 它计算相对于模型参数的损失梯度。
# 然后应用计算出的梯度来更新变量。

#4.训练模型

# tf.summary的用法 https://www.cnblogs.com/lyc-seu/p/8647792.html
tf.summary.scalar('loss',loss)
#用来显示标量信息
summaryMerged = tf.summary.merge_all()
#merge_all 可以将所有summary全部保存到磁盘，以便tensorboard显示。
filename = './movie_tensorborad'
writer = tf.summary.FileWriter(filename)
#指定一个文件用来保存图。
sess = tf.Session()
#https://www.cnblogs.com/wuzhitj/p/6648610.html
init = tf.global_variables_initializer()
sess.run(init)
#运行

for i in range(5000):
    _, movie_summary = sess.run([train, summaryMerged])
    # 把训练的结果summaryMerged存在movie里
    writer.add_summary(movie_summary, i)
    # 把训练的结果保存下来

#5评估模型
Current_X_parameters, Current_Theta_parameters = sess.run([X_parameters, Theta_parameters])
# Current_X_parameters为用户内容矩阵，Current_Theta_parameters用户喜好矩阵
predicts = np.dot(Current_X_parameters,Current_Theta_parameters.T) + rating_mean
# dot函数是np中的矩阵乘法，np.dot(x,y) 等价于 x.dot(y)
errors = np.sqrt(np.sum((predicts - rating)**2))
# sqrt(arr) ,计算各元素的平方根
print(errors)

#6.构建完整的电影推荐系统
user_id = input('您要想哪位用户进行推荐？请输入用户编号：')
sortedResult = predicts[:, int(user_id)].argsort()[::-1]
# argsort()函数返回的是数组值从小到大的索引值; argsort()[::-1] 返回的是数组值从大到小的索引值
idx = 0
print('为该用户推荐的评分最高的20部电影是：'.center(80,'='))
# center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
for i in sortedResult:
    print('评分: %.2f, 电影名: %s' % (predicts[i,int(user_id)],movies_df.iloc[i]['title']))
    # .iloc的用法：https://www.cnblogs.com/harvey888/p/6006200.html
    idx += 1
    if idx == 20:break