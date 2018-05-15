import time
import calendar


ticks=time.time()
localtime = time.localtime(ticks)
localtimeASC = time.asctime(localtime)

print("当前时间:",ticks,"\n本地时间:",localtime,"\n本地格式化的时间:",localtimeASC)

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)