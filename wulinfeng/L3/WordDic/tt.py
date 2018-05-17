class Person(object):

    def __init__(self,age,name):
        self.age = age
        self.name = name


def operatorSort():
    persons = [Person(age,name) for (age,name) in [(202,"lili"),(28,"lulu"),(16,"kaka"),(90,"xixi")]]
    print(type(persons))
    try:
        import operator
    except ImportError:
        cmpfun = lambda x:x.age
    else:
        cmpfun = operator.attrgetter("age","name")

    persons.sort(key = cmpfun, reverse=False)
    for element in persons:
        print(element.age, ":", element.name)
# def personSort():
#     persons = [Person(age,name) for (age,name) in [(12,"lili"),(18,"lulu"),(16,"kaka"),(12,"xixi")]]
#     persons.sort(cmp=None,key=lambda x:x.age,reverse=False)
#     for element in persons:
#         print (element.age,":",element.name)

operatorSort()