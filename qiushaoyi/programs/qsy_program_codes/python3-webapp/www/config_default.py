'''
   编写配置文件：数据库的用户名、口令以及不同环境的host配置等
   该文件为：开发环境的标准配置 ----> 本地服务
'''

configs = {
    'debug':True,
    'db': {
        'host':'www.baidu.com',
        'port':3306,
        'user':'root',
        'password':'qsy112933',
        'db':'awesome'
    },
    'session': {
        'secret':'Awesome'
    },
}
