from pandas import Series
import pandas as pd

#他如列表的一样的，一列数据，每个数据对应一个索引值
#Series就是竖起来的list
s = Series([1,4,'ww','tt'])
print(s)
print(s.index)
print(s.values)
#自定义索引
s2 = Series(['wangxing','man',24],index=['name','sex','age'])
print(s2)
s2['age'] = 12
print(s2)

#字典的方式
sd = {'python': 9000, 'c++': 9001, 'c#': 9000}
s3 = Series(sd)
print(s3)
#自定义索引呀，自动对齐，
s4 = Series(sd, index=['java', 'c++', 'c#'])
#判断值是否为空
print(pd.isnull(s4))
print(s4.isnull)
#重新定义索引名字
s4.index = ['Java','C++','C#']
print(s4[s4>9000])

'''series的运算'''