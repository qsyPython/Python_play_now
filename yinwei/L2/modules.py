#模块笔记
#本期模块3分享内容：
#常用内建模块（time、calendar、datetime、collections、
# base64、struct、hashlib、hmac、itertools、contextlib、
# urllib、XML、HTMLParser）


#time模块
import time
time.time() #它返回纪元开始的秒数，返回值为浮点数
time.ctime() #一般用于存储和比较日期，但是对人类不友好，要记录和打印时间，可以使用ctime()
time.clock() #返回处理器时钟时间
time.gmtime() #用于获取UTC时间   UTC时间实际就是格林尼治时间，它与中国时间的时差为八个小时。
time.localtime() #用于获取当前时区的当前时间
time.strptime() #用于将字符串时间转换成struct_time格式
time.strftime() #用于时间的格式化输出
time.mktime() #用于将struct_time转换成时间的浮点数表示
time.sleep()  #sleep函数用于将当前线程交出，要求它等待系统将其再次唤醒，如果写程序只有一个线程，这实际上就会阻塞进程，什么也不做。
time.altzone() #返回格林威治西部的夏令时地区的偏移秒数，如果该地区在格林威治东部会返回负值(如西欧，包括英国)，对夏令时启用地区才能使用

#用的比较多的就是这些。如果有特殊需求，请查看api

#calendar

import calendar
calendar.calendar(2018,w=2,l=1,c=6) #返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数
calendar.firstweekday() #返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一
calendar.isleap(2018) #2018是闰年返回True，否则为false。
calendar.leapdays(1990,2018) #返回在1990，2018两年之间的闰年总数。
calendar.month(1992,11,w=2,l=1)
#返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
calendar.monthcalendar(2016,11)
#返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
calendar.monthrange(2016,11)
#返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12
calendar.prcal(2015,w=2,l=1,c=6)
#相当于 print calendar.calendar(2015,2,1,6).

calendar.prmonth(2014,2,w=2,l=1,c=5)
#相当于 print calendar.calendar（2014，2，1，5）
calendar.setfirstweekday(1)
#设置每周的起始日期码。0（星期一）到6（星期日）。
calendar.timegm(tupletime)
#和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
calendar.weekday(2011,12,24)
#返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。


#