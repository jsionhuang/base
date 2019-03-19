import pythonmapreduce as reduce


#1.交换值
a = 3
b = 4
a,b = b,a
print(a,b)
#
#2.对数组按照绝对值进行排序
list1 = [3, 5, -4, -1, 0, -2, -6]
print(sorted(list1,key = lambda x:abs(x)))
#字典中进行排序
d1 = {'a':1,'b':4,'c':2}
d2 = {}
d2 = sorted(d1.items(),key= lambda  x:x[1],reverse=True)
print('字典中进行排序',d2)
print(list(filter(lambda x: x % 2 == 0, range(1, 21))))

#对象排序
l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
l = sorted(l,key=lambda x:x[1])
print(l)
for obj in l:
    print(type(obj))

l=[{'b': 1}, {'b': 2}, {'b': 6}, {'b': 4}, {'b': 3}]
l = sorted(l,key=lambda x:x['b'])
print(l)

#求20内数字的和
print('求20内数字的和',list(map(lambda x:x*x ,range(1,21))))


#求1到100之间的和
print('求1到100之间的和',reduce(lambda x,y:x+y,range(1,101)))

