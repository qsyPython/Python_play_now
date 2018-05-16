# 按照指定格式将Python数据转换为字符串,
# 该字符串为字节流, 如网络传输时, 不能传输int, 此时先将int转化为字节流, 然后再发送;
# 按照指定格式将字节流转换为Python指定的数据类型;
# 处理二进制数据, 如果用struct来处理文件的话, 需要用’wb’, ’rb’以二进制(字节流)
# 写, 读的方式来处理文件;
# 处理c语言中的结构体;
#     函数 	                            return 	                               explain
# pack(fmt,v1,v2…) 	                string 	按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
# pack_into(fmt,buffer,offset,v1,v2…) 	 None 	按照给定的格式(fmt),将数据转换成字符串(字节流),并将字节流写入以offset开始的buffer中.(buffer为可写的缓冲区,可用array模块)
# unpack(fmt,v1,v2…..) 	            tuple 	按照给定的格式(fmt)解析字节流,并返回解析结果
# pack_from(fmt,buffer,offset) 	        tuple 	按照给定的格式(fmt)解析以offset开始的缓冲区,并返回解析结果
# calcsize(fmt) 	size of fmt 	计算给定的格式(fmt)占用多少字节的内存，注意对齐方式