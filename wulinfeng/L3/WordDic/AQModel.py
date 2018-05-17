class AQModel(object):

    def __init__(self,name,aqiValue):
        self.name = name
        self.aqiValue = aqiValue


    def Cons(self):
        print(self.name,'的AQI值是',self.aqiValue)
