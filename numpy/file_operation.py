#导入不同的文件名 pandas是为了解决数据分析创建的，pandas纳入了大量库和一些标准的数据模型
#从：csv，txt，exce 文件，数据库：mysql等。

import pandas as pd
filepath  = 'D:\\QQLoad\\software2.csv'

#sep是指定分隔符
df = pd.read_csv(filepath,encoding='utf-8')
print(df.head(3))
