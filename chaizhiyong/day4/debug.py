# import urllib.request
#
# httpHandler = urllib.request.HTTPHandler(debuglevel=1)
# httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
# opener = urllib.request.build_opener(httpHandler)
# urllib.request.install_opener(opener)
# response = urllib.request.urlopen('http://www.baidu.com')
# with open("url_response.txt", "w") as f:
#     print(response.read(), file=f)

import urllib.request
import http.client

http.client.HTTPConnection.debuglevel = 1

response = urllib.request.urlopen('http://www.baidu.com')
with open("url_response.txt", "w") as f:
    print(response.read(), file=f)