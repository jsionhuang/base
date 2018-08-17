
import time
#将字符串的时间转换为时间戳
t = "2017-11-24 17:30:00"
#将其转换为时间数组
timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
#转换为时间戳:
timeStamp = int(time.mktime(timeStruct))
print(timeStamp)

#时间戳转换为指定格式日期
timeStamp = 1511515800
localTime = time.localtime(timeStamp)
strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
print(strTime)

#格式切换
t = "2017-11-24 17:30:00"
#先转换为时间数组,然后转换为其他格式
timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
strTime = time.strftime("%Y/%m/%d %H:%M:%S", timeStruct)
print(strTime)

# 获取当前时间并转换为指定日期格式
now = int(time.time())
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeStruct = time.localtime(now)
strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
print(strTime)

#获得三天前的时间的方法
import datetime
#先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
#转换为时间戳:
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
#转换为其他字符串格式:
strTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(strTime)

#使用datetime模块来获取当前的日期和时间
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是 %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)