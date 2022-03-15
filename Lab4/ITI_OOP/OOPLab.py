import re
##################################### Person Class ################################
class Person:
    moods = ("happy", "tired", "lazy")
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.mood = "0"
        self.healthRate =0

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, val):
        if isinstance(val, int):
            if val > 100:
                self.__healthRate = 100
            elif val < 0:
                self.__healthRate = 0
            else:
                self.__healthRate = val


    def sleep(self, hours):
        if isinstance(hours, int):
            if hours > 7:
                self.mood = "lazy"
            elif hours < 7 :
                self.mood = "tired"
            else:
                self.mood = "happy"
        else:
            raise Exception("Sleep should take a number hours")
    def eat(self, meals):
        if isinstance(meals, int):
            if meals == 3:
                self.__healthRate = "100%"
            elif meals == 2 :
                self.__healthRate = "75%"
            elif meals == 1:
                self.__healthRate = "50%"
            else:
                print("Enter The number of meals (1 , 2, 3)")
        else:
            raise Exception("eat should take a number of meals")
    def buy(self, items):
        if (self.money-10*items > 0):
            self.money -= 10*items
        else:
            print("No Enough Money ")

# x = Person("zahra", 1000)
# print(x.mood)
# x.sleep(7)
# print(x.mood)
# print(x.healthRate)
# x.eat(2)
# print(x.healthRate)
# print(x.money)
# x.buy(2)
# print(x.money)
# x.buy(2)
# print(x.money)

######################################## Employee Class ############################
class Employee(Person):

    def __init__(self,id,name, money, car, email, salary, distanceToWork):
        Person.__init__(self, name, money)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, val):
        mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(mail_regex, val)):
            raise Exception ("Invalid Email")
        else:
            self.__email = val


    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, val):
        if isinstance(val, int):
            self._salary = 1000
            if val > 1000:
                self.__salary = val
            else:
                raise Exception ("Salary must be greater than 1000")
        else:
            raise Exception ("Salary must be a number")

    def work(self, hours):
        if isinstance(hours, int):
            if hours < 8:
                self.mood = "lazy"
            elif hours > 8:
                self.mood = "tired"
            else:
                self.mood = "happy"
        else:
            raise Exception("Work should take a number hours")

    def drive():
        print("Hello from drive")
    def refuel():
        print("Hello from refuel")
    def send_mail():
        print("Hello from send_mail")

# y = Employee(1,"zahra",1000,'fiat',"zahra@gmail.com",10000,100)
# print(y.email)
# print(y.salary)
# print(y.healthRate)
# y.eat(1)
# print(y.healthRate)
# print(y.mood)
# y.work(8)
# print(y.mood)
######################################## Office Class #############################
class Office():
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

        def get_all_employees(self):
            print(self.Employees)
        def get_employee(self):
            pass
        def hire(self):
            pass
        def fire(self):
            pass
        def calculate_lateness(self):
            pass
        def deduct(self):
            pass
        def reward(self):
            pass

################################### Car Class ######################################
class Car():
    def __init__(self, name):
        self.name = name
        self.fuelRate = 0
        self.velocity = 0

    @property
    def fuelRate(self):
        pass
    @property
    def velocity(self):
        pass

    def run(self):
        pass
    def stop(self):
        pass











