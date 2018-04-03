#如何在列表，字典，集合中根据条件筛选数据？


data = [1,2,3,-3,-25,0,9]

res = []

for x in data:
    if x >=0:
        res.append(x)
print(res)