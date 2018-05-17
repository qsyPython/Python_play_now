class hw2:
    empCount = 0



    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        hw2.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % hw2.empCount

    def displayEmployee(self):
        print( "Name : ", self.name, ", Salary: ", self.salary)




