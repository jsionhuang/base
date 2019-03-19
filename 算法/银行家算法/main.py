'''
两大功能模块
1.给出进程数，资源数，进程需要资源数，进程已占有资源数，给出是否安全，若安全给出安全序列
2.模拟里面进程请求资源，预测本次操作是否安全
'''

import copy

#模拟进程请求资源
def simulationReques(process_id,request_dict):
    print('Now Allocation:',allocation)
    #最大请求数 >= 请求数 ？
    if not compareDict(max[process_id],request_dict):
        print('请求资源过大，拒绝')
        return False
    #可用资源 >= 请求数？
    if not compareDict(avaiable,request_dict):
        print('无足够资源分配，拒绝')
        return False
    #分配资源
    subtractionDict(avaiable,request_dict)#可用资源减少
    addDict( allocation[process_id],request_dict)#进程占用资源增加
    subtractionDict( need[process_id],request_dict)#进程需要资源减少

    #系统安全性检查
    if calculateSafe(avaiable,need,allocation,pn):
        print('okay')
    else:
        addDict(avaiable, request_dict)
        subtractionDict(allocation[process_id], request_dict)
        addDict(need[process_id], request_dict)
    return allocation



#安全性算法函数
#avaible-可用资源,need--需要资源,allocation-已占有资源,pn-进程数
def calculateSafe(avaiable,need,allocation,pn):
    #copy 可用资源数
    avaible_work = copy.deepcopy(avaiable)
    #创建完成数组，默认设为全0-False
    finsh_arr = [0] * pn
    #创建安全序列
    safe_queue = []
    #循环5次
    count = 0
    print('Avaiable_Work:',avaible_work)
    print('Finsh_Arr:',finsh_arr)
    print('Safe_Queue:',safe_queue)
    while count < pn:
        #按进程编号找到一个可安全加入进程的进程
        i = 0
        while i < pn:
            # 该进程未完成模拟
            if not finsh_arr[i]:
                #可用资源 >= 请求资源 ？
                is_safe = compareDict(avaible_work,need[i])
                if is_safe:#如果成功
                    # 更新安全队列
                    safe_queue.append(i)
                    # 更新完成值
                    finsh_arr[i] = True
                    # 更新可用资源 = 当前可用 + 当前进程释放资源
                    addDict(avaible_work,allocation[i])

            i += 1
        count += 1
    print('Avaiable_Work:', avaible_work)
    print('Finsh_Arr:', finsh_arr)
    print('Safe_Queue:', safe_queue)
    if len(safe_queue) == pn:
        print('系统处于安全状态，计算得出安全序列',safe_queue)
        return True
    print('不安全')
    return False



#比较两个字典,如果a>=b返回true
def compareDict(a,b):
    flag = True
    for key in a.keys():
        if a[key] < b[key]:
            return False
    return flag
#两个字典相加a的值增加b的值
def addDict(a,b):
    for key in a.keys():
        a[key] = a[key] + b[key]
#两个字典相减 a的值减少b的值
def subtractionDict(a,b):
    for key in a.keys():
        a[key] = a[key] - b[key]





if __name__ == '__main__':
    #进程数 = 下面数组的长度
    pn = 5
    #各种资源总资源数
    avaiable = { "A":3,"B":12,'C':14,'D':14}
    #每个进程对各种资源的最大需求
    max = [
        {"A": 0, "B": 0, 'C': 4, 'D': 4},
        {"A": 2, "B": 7, 'C': 5, 'D': 0},
        {"A": 3, "B": 6, 'C': 10, 'D': 10},
        {"A": 0, "B":9, 'C': 8, 'D': 4},
        {"A": 0, "B": 6, 'C': 6, 'D': 10}
    ]
    #各个进程已占有的资源数
    allocation = [
        {"A": 0, "B": 0, 'C': 3, 'D': 2},
        {"A": 1, "B": 0, 'C': 0, 'D': 0},
        {"A": 1, "B": 3, 'C': 5, 'D': 4},
        {"A": 0, "B": 3, 'C': 3, 'D': 2},
        {"A": 0, "B": 0, 'C': 1, 'D': 4}
    ]

    #得到进程资源的需求数 = 最大需求 - 已占有
    need = []
    cn = 0
    for i in range(pn):
        tmp = copy.deepcopy(max[i])
        subtractionDict(tmp,allocation[i])
        need.append(tmp)
        cn += 1
    print('Need:',need)
    #各个资源的可用数量 = 资源总数 - 已占有
    for allo in allocation:
        subtractionDict(avaiable,allo )
    print("Avaiable:",avaiable)

    #调用方法，判断当前进程是否安全
    calculateSafe(avaiable, need, allocation, pn)

    #模拟进程请求资源
    args_process_id = 2#进程2的最大请求数为{"A": 3, "B": 6, 'C': 10, 'D': 10}
    args_request_dict = {'A': 0, 'B': 0, 'C': 2, 'D': 2}#请求资源数情况
    print(simulationReques(args_process_id, args_request_dict))

