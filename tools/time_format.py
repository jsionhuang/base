import datetime

#输入两个时间段返回 中间全部的日期的集合
def getEachDay(start_day,end_day):
    d1 = datetime.datetime.strptime(start_day, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(end_day, '%Y-%m-%d')
    print(d1 -d2)
    datelist = []
    while d1 <= d2:
        d_str = d1.strftime('%Y-%m-%d')
        datelist.append(d_str)
        d1 += datetime.timedelta(days=1)
    return datelist