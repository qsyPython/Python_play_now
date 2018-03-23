import os
mystr1 = "ls"
b = os.popen('ls')
b.read()
os.system(mystr1)

