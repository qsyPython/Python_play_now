class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)
    def tomorrow(self):
        self.day +=1
    @staticmethod
    def parse_from_string(data_str):
        year,month,day = tuple(data_str.split("-"))
        return Date(int(year),int(month),int(day))
if __name__  == '__main__':
    new_day = Date(2018,12,31)
    new_day.tomorrow()

    date_str = "2018-12-13"
    new_1 = Date.parse_from_string(date_str)

    print(new_1)
    #print(new_day)
