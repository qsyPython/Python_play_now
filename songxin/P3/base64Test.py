import base64

a = base64.b64encode(("qwertyuiop").encode(encoding='utf-8')).decode()
b = base64.b64decode(a).decode()
print(a)
print(b)