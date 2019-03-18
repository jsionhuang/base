l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
l = sorted(l,key=lambda x:x[1])
print(l)


l=[{'b': 1}, {'b': 2}, {'b': 6}, {'b': 4}, {'b': 3}]
l = sorted(l,key=lambda x:x['b'])
print(l)