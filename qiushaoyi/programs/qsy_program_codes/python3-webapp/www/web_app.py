'''
	作者：邱少一
	日期：2018/03/06
	1、准备：

	python版本：python3 --version
	选择Web异步的框架aiohttp：pip3 install aiohttp(比较底层，需要再次封装)
	前端模板引擎jinja2：pip3 install jinja2
	MySQL的Python异步驱动程序aiomysql：pip3 install aiomysql
	监控目录文件变化：pip3 install watchdog


	2、流程：
	1、编写web 骨架
	2、编写ORM 和 Model
	3、编写 web框架（基于aiohttp）
	4、编写配置文件
	5、编写MVC
	6、构建前端
	7、编写API（返回的是机器可解析的数据，而不是HTML 的URL这样的就是API）：如果一个URL返回的不是HTML，而是机器能直接解析的数据，这个URL就可以看成是一个Web API
    8、用户注册登陆：（ 用户口令是客户端传递的经过SHA1计算后的40位Hash字符串，所以服务器端并不知道用户的原始口令；
    服务器要跟踪web用户的登陆状态，只能通过客户端cookie实现，web端保存在Session中。。。
    Session的优点可直接读取，缺点是服务器需要在内存中维护：1个映射表，来存储用户登录信息，
    问题是，多台服务器时，需要Session做集群，另1个服务器为Redis：存储各个服务器中的Session，然后对通过Redis和服务端进行交互 ）

    （实际开发：不这么操作）🙋解决方案：采用直接读取cookie的方式来验证用户登录，每次用户访问任意URL，都会对cookie进行验证。保证服务器处理任意的URL：都是无状态的，可以扩展到多台服务器。

    9、编写日志：Vue这个MVVM框架：来实现创建Blog的页面 和 页面分页，维护成本变得更低

    10、提升开发效率：django 可以在debug模式下自动重新加载，保证开发过程中同步性；
    我们没有django处理上，我们解决方案：检测www目录下的代码改动，一旦有改动，就自动重启服务器。
    编写一个辅助程序pymonitor.py
    功能：1、检测www目录下的代码改动  2、把当前wsgiapp.py进程杀掉  3、重启服务
    最终实现了： Debug模式的自动重新加载

    11、完成web app：
    12、部署 web开发服务器
    编写移动app



0、
Web框架：基于asyncio的aiohttp

1、HTTP请求的流程3步走：
#
# 步骤1：浏览器首先向服务器发送HTTP请求，请求包括：
#
# 请求方式：GET还是POST，GET仅请求资源，POST会附带用户数据；
# 域名：由Host头指定：Host: www.sina.com.cn
# 路径：/full/url/path；
# Header：其他相关的Header；
# 如果是POST，那么请求还包括一个可选的Body，包含用户数据。
#
# 步骤2：服务器向浏览器返回HTTP响应，响应内容包括：
#
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
# 响应类型：由Content-Type指定；
# Header：以及其他相关的Header；
# 通常服务器的HTTP响应会携带内容，也就是有一个Body：包含响应的内容，网页的HTML源码就在Body中。
#
# 步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

2、
async：使用场景 -> 异步网络操作、并发、协程！！！等效于 @asyncio.coroutine
await： 用于挂起阻塞的异步调用接口 ！！！ 等效于 yield from
'''

import logging;logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web,web_runner
from jinja2 import Environment, FileSystemLoader

from config import configs

import orm
from coroweb import add_routes, add_static

from handlers import cookie2user, COOKIE_NAME


'''
========================== 0:初始化前端模板  ==========================
app的模板 绑定为env
'''
def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(BASE_DIR, 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        logging.info('logger_factory -> Request: %s %s' % (request.method, request.path))
        # yield from asyncio.sleep(0.3)
        return (yield from handler(request))
    return logger

# 对于每个URL处理函数，如果我们都去写解析cookie的代码，那会导致代码重复很多次。
# 利用middle在处理URL之前，把cookie解析出来，并将登录用户绑定到request对象上
@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        if cookie_str:
            user = yield from cookie2user(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        return (yield from handler(request))
    return auth

@asyncio.coroutine
def data_factory(app, handler):
    @asyncio.coroutine
    def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = yield from request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = yield from request.post()
                logging.info('request form: %s' % str(request.__data__))
        return (yield from handler(request))
    return parse_data

# 获取请求体
@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html'
            resp.charset = 'utf-8'
            return resp
        if isinstance(r, dict): # 模板的请求返回内容
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                r['__user__'] = request.__user__
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and r >= 100 and r < 600:
            return web.Response(r)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response


def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

'''
========================== 暂时放这儿调试用 -> 1: 路由 ==========================
'''
# body：为显示html的body，要不然一片空白
# 内容类型为text/html，要不然会被当做file执行下载；
# body中字符的编码charset：utf-8，要不然中文会乱码

def index(request):
    logging.info('server response...')
    r = web.Response()
    r.body = '<h1> Awesome </h1>'
    r.content_type = 'text/html'
    r.charset = 'utf-8'
    return r

def hello(request):
    logging.info('我要访问接口了...')
    hello_text = '<h1> 我就是帅,哈哈哈 </h1>'
    r = web.Response()
    r.body = hello_text
    r.content_type = 'text/html'
    r.charset = 'utf-8'
    return r

'''
========================== 2: 初始化loop ==========================
'''

@asyncio.coroutine
def init(loop):
    # 创建数据库池：数据库的账户和密码，以及db需要首先创建好！！！
    yield from orm.create_pool(loop=loop,**configs.db)

    # middleware是一种拦截器,URL在被某个函数处理前,可以经过一系列的 middleware 的处理
    app = web.Application(loop=loop,middlewares=[
        logger_factory,auth_factory,response_factory
    ])
    # 适配python3.0
    app = web_runner.AppRunner(app=app).app
    # 手动添加路由:
    app.router.add_route('GET','/testIndex',index)
    app.router.add_route('GET','/testHello',hello)

    # 初始化模板引擎：绑定了block 和
    init_jinja2(app,filters=dict(datetime=datetime_filter))
    # 给web app添加路由，统一放在handlers模块中处理
    add_routes(app,'handlers')
    # 注册静态文件
    add_static(app)

    logging.info('server before...')

    # 创建1个服务器对象
    host = '127.0.0.1'
    port = 9000
    server = yield from loop.create_server(app.make_handler(),host,port)
    logging.info('server start at http://%s:%s' % (host,port))
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever() # server 才会执行listen



