#psutil是一个跨平台库（http://code.google.com/p/psutil/），能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。它主要应用于系统监控，分析和限制系统资源及进程的管理

import psutil
#使用cpu_times获取cpu的完整信息
#print(psutil.cpu_times())#scputimes(user=6157.05, nice=0.0, system=3130.85, idle=177492.17)

#psutil.cpu_count()#获取cpu的逻辑个数
#print(psutil.cpu_count()) #8

#获取cpu的所有逻辑信息
#print(psutil.cpu_times_percent())#scputimes(user=0.0, nice=0.0, system=0.0, idle=0.0)
#获取内存的所有信息
#print(psutil.virtual_memory())#svmem(total=17179869184, available=6949957632, percent=59.5, used=10303217664, free=5019918336, active=6379835392, inactive=1930039296, wired=1993342976)

#获取磁盘的详细信息
#print(psutil.disk_partitions())#[sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]

#返回当前登录系统的用户信息
print(psutil.users())#suser(name='yinwei', terminal='console', host=None, started=1526260224.0, pid=100), suser(name='yinwei', terminal='ttys000', host=None, started=1526268416.0, pid=785), suser(name='yinwei', terminal='ttys002', host=None, started=1526278912.0, pid=2704)]


