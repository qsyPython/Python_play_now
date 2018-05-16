
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48,122)) for  i  in  range(20)])
        self.password = get_md5(password+self.salt)


db = {}

def register(username,password):
    db[username] = User(username,password)
    return True

def login(username,password):
    user = db[username]
    return user.password == get_md5(password + user.salt)



assert register('michael', '123456')
assert register('bob', 'abc999')
assert register('alice', 'alice2008')


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')

print()
print('ok')