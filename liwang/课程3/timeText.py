#!/usr/bin/python

import calendar

print(calendar.calendar(theyear=2018,w=2,l=1,c=10))

#返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。
# 每行长度为21* W+18+2* C。l是每星期行数。


print(calendar.firstweekday( ))

#返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。

print('%s' % calendar.isleap(year= 2018))

#是闰年返回True，否则为false。

print(calendar.leapdays(y1=1020,y2=2018))

#闰年总数

print(calendar.month(theyear= 2018,themonth=1 ,w=2,l=1))

# 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。

print(calendar.monthcalendar(year= 2018,month= 1))

#返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。

print(calendar.monthrange(year= 2018,month= 2))

# 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。

print(calendar.prcal(theyear= 2018,w=2,l=1,c=6))
# calendar.prmonth(year,month,w=2,l=1)
# 相当于 print calendar.calendar(year,w,l,c).

print(calendar.setfirstweekday(firstweekday= 6))
# 设置每周的起始日期码。0（星期一）到6（星期日）

import time

print(time.gmtime())
print(calendar.timegm(tuple= (2018, 4, 25, 11, 19, 0, 0, 0, 0)))
# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。

print(calendar.weekday(year= 2018, month= 2, day= 13))
# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。

"""
Time类
    time类表示时间，由时、分、秒以及微秒组成。（我不是从火星来的~~）time类的构造函数如下：

    class datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ) ：各参数的意义不作解释，这里留意一下参数
    tzinfo，它表示时区信息。注意一下各参数的取值范围：hour的范围为[0, 24)，minute的范围为[0, 60)，second的范围为[0, 60)，
    microsecond的范围为[0, 1000000)。

    time类定义的类属性：

time.min、time.max：time类所能表示的最小、最大时间。其中，time.min = time(0, 0, 0, 0)， time.max = time(23, 59, 59, 999999)；
time.resolution：时间的最小单位，这里是1微秒；
    time类提供的实例方法和属性：

time.hour、time.minute、time.second、time.microsecond：时、分、秒、微秒；
time.tzinfo：时区信息；
time.replace([ hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )：创建一个新的时间对象，用参数指定的时、分、秒、
微秒代替原有对象中的属性（原有对象仍保持不变）；
time.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
time.strftime(fmt)：返回自定义格式化字符串。在下面详细介绍；
"""


from  datetime  import  *

tm = time(23 ,  46 ,  10 )
print  ('tm:' , tm  )
print  ('hour: %d, minute: %d, second: %d, microsecond: %d'  \
        % (tm.hour, tm.minute, tm.second, tm.microsecond)  )
tm1 =  (tm.replace(hour = 20 )  )
print  ('tm1:' , tm1 )
print  ('isoformat():' , tm.isoformat()  )

"""
  date提供的实例方法和属性：

date.year、date.month、date.day：年、月、日；
date.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
date.timetuple()：返回日期对应的time.struct_time对象；
date.toordinal()：返回日期对应的Gregorian Calendar日期；
date.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
data.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
date.isocalendar()：返回格式如(year，month，day)的元组；
date.isoformat()：返回格式如'YYYY-MM-DD’的字符串；
date.strftime(fmt)：自定义格式化字符串。在下面详细讲解。
"""

now = date( 2010 ,  4 ,  6 )
tomorrow = now.replace(day = 7 )
print   ('now:' , now,  ', tomorrow:' , tomorrow)
print   ('timetuple():' , now.timetuple())
print   ('weekday():' , now.weekday())
print   ('isoweekday():' , now.isoweekday())
print   ('isocalendar():' , now.isocalendar())
print   ('isoformat():' , now.isoformat())

"""
 date还对某些操作进行了重载，它允许我们对日期进行如下一些操作：

date2 = date1 + timedelta  # 日期加上一个间隔，返回一个新的日期对象（timedelta将在下面介绍，表示时间间隔）
date2 = date1 - timedelta   # 日期隔去间隔，返回一个新的日期对象
timedelta = date1 - date2   # 两个日期相减，返回一个时间间隔对象
date1 < date2  # 两个日期进行比较
    注： 对日期进行操作时，要防止日期超出它所能表示的范围。
"""

now = date.today()
tomorrow = now.replace(day = 7 )
delta = tomorrow - now
print  ('now:' , now,  ' tomorrow:' , tomorrow  )
print  ('timedelta:' , delta  )
print  (now + delta  )
print  (tomorrow > now )
import datetime
# datetime.datetime()
"""
datetime类
    datetime是date与time的结合体，包括date与time的所有信息。它的构造函数如下：
    datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )，
    各参数的含义与date、time的构造函数中的一样，要注意参数值的范围。

    datetime类定义的类属性与方法：

datetime.min、datetime.max：datetime所能表示的最小值与最大值；
datetime.resolution：datetime最小单位；
datetime.today()：返回一个表示当前本地时间的datetime对象；
datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
datetime.utcnow()：返回一个当前utc时间的datetime对象；
datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
datetime.combine(date, time)：根据date和time，创建一个datetime对象；
datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；
"""

# print   ('datetime.max:' , datetime.datetime.max)
# print   ('datetime.min:' , datetime.datetime.min)
# print   ('datetime.resolution:' , datetime.datetime.resolution)
# print   ('today():' , datetime.datetime.today())
# print   ('now():' , datetime.now())
# print   ('utcnow():' , datetime.utcnow())
# print   ('fromtimestamp(tmstmp):' , datetime.datetime.fromtimestamp('1524655140'.encode("utf-8")))
# #time.time()
# print   ('utcfromtimestamp(tmstmp):' , datetime.datetime.utcfromtimestamp(time.time()))

"""
datetime类提供的实例方法与属性（很多属性或方法在date和time中已经出现过，在此有类似的意义，
这里只罗列这些方法名，具体含义不再逐个展开介绍，可以参考上文对date与time类的讲解。）：

datetime.year、month、day、hour、minute、second、microsecond、tzinfo：
datetime.date()：获取date对象；
datetime.time()：获取time对象；
datetime. replace ([ year[ , month[ , day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] ] ] ])：
datetime. timetuple ()
datetime. utctimetuple ()
datetime. toordinal ()
datetime. weekday ()
datetime. isocalendar ()
datetime. isoformat ([ sep] )
datetime. ctime ()：返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
datetime. strftime (format)
    像date一样，也可以对两个datetime对象进行比较，或者相减返回一个时间间隔对象，或者日期时间加上一个间隔返回一个新的日期时间对象。
    这里不提供详细的例子，看客自己动手试一下~~

格式字符串
    datetime、date、time都提供了strftime()方法，该方法接收一个格式字符串，输出日期时间的字符串表示。
    下表是从python手册中拉过来的，我对些进行了简单的翻译（翻译的有点噢口~~）。

格式字符  意义

%a 星期的简写。如 星期三为Web
%A 星期的全写。如 星期三为Wednesday
%b 月份的简写。如4月份为Apr
%B月份的全写。如4月份为April 
%c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
%d:  日在这个月中的天数（是这个月的第几天）
%f:  微秒（范围[0,999999]）
%H:  小时（24小时制，[0, 23]）
%I:  小时（12小时制，[0, 11]）
%j:  日在年中的天数 [001,366]（是当年的第几天）
%m:  月份（[01,12]）
%M:  分钟（[00,59]）
%p:  AM或者PM
%S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
%U:  周在当年的周数当年的第几周），星期天作为周的第一天
%w:  今天在这周的天数，范围为[0, 6]，6表示星期天
%W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
%x:  日期字符串（如：04/07/10）
%X:  时间字符串（如：10:43:39）
%y:  2个数字表示的年份
%Y:  4个数字表示的年份
%z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z:  时区名称（如果是本地时间，返回空字符串）
%%:  %% => %
"""

dt = datetime.datetime.now()
print   ('(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S %f' )  )
print   ('(%Y-%m-%d %H:%M:%S %p): ' , dt.strftime( '%y-%m-%d %I:%M:%S %p' )  )
print   ('%%a: %s '  % dt.strftime( '%a' )  )
print   ('%%A: %s '  % dt.strftime( '%A' )  )
print   ('%%b: %s '  % dt.strftime( '%b' )  )
print   ('%%B: %s '  % dt.strftime( '%B' )  )
print   ('日期时间%%c: %s '  % dt.strftime( '%c' )  )
print   ('日期%%x：%s '  % dt.strftime( '%x' ) )
print   ('时间%%X：%s '  % dt.strftime( '%X' ) )
print   ('今天是这周的第%s天 '  % dt.strftime( '%w' ))
print   ('今天是今年的第%s天 '  % dt.strftime( '%j' ) )
print   ('今周是今年的第%s周 '  % dt.strftime( '%U' )  )

