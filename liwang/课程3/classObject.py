
class person:
    def __init__(self,name,sex):
        self.__name = name 
        self.__sex = sex
    
    @property
    def name(self):
        return self.__name;
    @name.setter
    def name(self,value):
        self.__name =  value

    