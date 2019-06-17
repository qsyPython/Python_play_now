import unittest
from L3_ErrorDebugTest import Dict


# 该类中对 Dict 做了5个测试
class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 最常用的断言就是assertEqual(): 判断2个参数时候相同
        self.assertEqual(d.b, 'test')
        self.assertEqual(isinstance(d, dict), True)

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):  # 连接数据库
        print('setUp...')

    def tearDown(self):  # 关闭数据库
        print('tearDown...')


# 就可以把mydict_test.py当做正常的python脚本运行
if __name__ == '__main__':
    unittest.main()
