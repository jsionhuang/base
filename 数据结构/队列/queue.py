from collections import deque
#一端只能删除，一段稚嫩给添加
queue = deque(["Eric", "John", "Michael"])
queue.append('Terry')
queue.append('dramam')
queue.popleft()
print(queue)
queue.popleft()
print(queue)
