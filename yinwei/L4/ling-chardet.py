#chardet 检测编码
import chardet
#print(chardet.detect(b'hello,world')) #'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
#confidence 字段表示的是检测的概率，1.0为100%
# data = '离离原上草，一岁一枯荣'.encode('gbk')
# print(chardet.detect(data))
#{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

# data = '离离原上草，一岁一枯荣'.encode('utf-8')
# print(chardet.detect(data))
#{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

# data = '最新の主要ニュース'.encode('euc-jp')
# print(chardet.detect(data))
{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
