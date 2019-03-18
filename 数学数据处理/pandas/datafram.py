from pandas import Series,DataFrame
#dataFram 二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式
data = {"name": ['google', 'baidu', 'yahoo'], "marks": [100, 200, 300], "price": [1, 2, 3]}
df1 = DataFrame(data)
print('通过字典生成的 datafrom')
print(df1)
#在 DataFrame 中，columns 跟字典键相比，有一个明显不同，就是其顺序可以被规定
df2 = DataFrame(data,columns=['name','price','marks'])
print('自定义索引顺序后的DataFrom')
print(df2)
#DataFrame 数据的索引也能够自定义
df3 = DataFrame(data,columns=['name','price','marks'],index=['a','b','c'])
print('自定义后的索引')
#字典套字典
#在字典中就规定好数列名称（第一层键）和每横行索引（第二层字典键）以及对应的数据（第二层字典值）
newdata = {'lang':{'first':'python','second':'java'},'price':{'first':5000,'second':2000}}
df4 = DataFrame(newdata)
print('字典套字典')
print(df4)
df5 = DataFrame(newdata,index=['first','second','third'])
print('自由换索引后')
print(df5)
#修改数据
df5['lang']['first'] = 'Python1'
