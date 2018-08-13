'''
	作者：邱少一
	日期：2018/03/06
	功能：
	 模块1：
     常用内建模块（time、calendar、datetime、collections、base64、struct、
     hashlib、hmac、itertools、contextlib、urllib、XML、HTMLParser）
'''
import time
# from datetime import datetime #从datetime模块中导入该datetime类
import datetime  # 导入该模块

# 1、time
# ticks = time.time() #1970纪元后到现在经过的浮点秒数
# local_ticks = time.localtime(time.time())
# local_format_tuple = time.strftime('%Y-%m-%d %H:%M:%S %j',local_ticks)
# print(local_ticks,'\n',local_format_tuple)

# 2、datetime
now = datetime.datetime.now()
dt = datetime.datetime(2015, 4, 19, 12, 20, 7)  # 用指定日期时间创建datetime

timeStr = dt.timestamp()
dt_back = datetime.datetime.fromtimestamp(timeStr)

cday = datetime.datetime.strftime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(now, dt, timeStr, dt_back, cday)
