class Date:
    def __init__(self,year,moth,day):
        self.year = year
        self.moth = moth
        self.day = day

    def tomorrow(self):
        self.day+=1

    @staticmethod
    def parse_from_string(data_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls,date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))


    def __str__(self):
        return "{year}/{moth}/{day}".format(year=self.year,moth=self.moth,day=self.day)

if __name__ =="__main__":
   #new_date= Date(2018,12,31)


    date_str = "2018-06-02"
    # year,month,day = tuple(date_str.split("-"))
    # new_date = Date(int(year),int(month),int(day))
    #print(new_date)
    new_date = Date.parse_from_string(date_str)
    print(new_date)