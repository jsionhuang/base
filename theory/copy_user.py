import copy

#原始数据
a = alist=[1,2,3,["a","b"]]
#赋值
b = a
#浅拷贝
c1 = a.copy()
#深拷贝
c2 = copy.deepcopy(a)
a.append(5)
a[3].append('c')
print('同时修改对象（增加对象），和修改子对象')
print('赋值',b,a == b)
print('浅拷贝',c1,a==c1)
print('深拷贝',c2,a==c2)
