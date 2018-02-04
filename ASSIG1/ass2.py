# class Person
class Person :
    name = ''
    money = 0
    moods = ['happy','tired','lazy']
    mood = ''
    healthRate = 0

    def __init__(self, name, money, healthRate):
        self.name = name 
        self.money = money  
        self.healthRate = healthRate  

    @property
    def healthRate(self):
    return self.__healthRate 


    def sleep(self,hours):
        if hours==7:
            self.mood = moods[0] 
        if hours<7:
            self.mood = moods[1]
        if hours>7:
            self.mood = moods[2]


    def eat(self,meals):
        if meals==3:
            self.healthRate = 100% 
        if meals==2:
            self.healthRate = 75%
        if meals==1:
            self.healthRate = 50%

    def buy(self,items):
        if items==1:
            money = money-10


# class Employee
class Employee(Person) :
    id = 0
    car = ''
    salary = 1000
    distanceToWork = 0
    email = ''

    def __init__(self, id, car, email, salary, distanceToWork):
        super(Employee, self).__init__(name, money, mood, healthRate)
        self.id = id 
        self.car = car
        self.salary = salary 
        self.email = email
        self.distanceToWork =distanceToWork  
        empCar = Car(self.name) 
        empOffice = Office(self.id)

        if self.salary < 1000:
        self.salary=1000

        if self.healthRate > 100 
            self.healthRate=100

    @property
    def salary(self):
    return self.__salary

    @property
    def email(self):
    return self.__email

   

    def work(self,hours):
        if hours==8:
            self.mood = 'happy' 
        if hours>8:
            self.mood = 'tired'
        if hours<8:
            self.mood = 'lazy'


    def drive(self,distance):
        driveTime=self.distanceToWork/empCar.velocity
        empCar.fuelRate=(empCar.fuelRate*0.1)*(distance/10)
        

    def refuel(self,gasAmount = 100):
         empCar.fuelRate= empCar.fuelRate+gasAmount


# class Office
class Office :
    name = ''
    employees = [] 

    def __init__(self, name='iti', empId):
        self.name = name 
        self.employees.append(empId)  
         
    @staticmethod
    def get_all_employees(self):
        for i in employees :
            print(i) 
        
    @staticmethod
    def  get_employee(self,empId):
        for i in employees :
            if i == empId :
                print(empId)
            else :
                print('no employee has that id')
        

    def hire(self):
       

    def fire(self):
       
    def calculate_lateness(self):
       

    def deduct(self):
       

    def reward(self):
       
       


# class Employee
class Car :
    name = ''
    fuelRate = 0
    velocity = 0

    def __init__(self, name, fuelRate=100, velocity=200):
        self.name = name
        self.fuelRate = fuelRate 
        self.velocity =velocity     

        if self.velocity > 200 :
            self.velocity=200
        
        if self.fuelRate > 100:
            self.fuelRate=100

    def run(self, velocity, distance):
        self.velocity = velocity
        self.fuelRate=(self.fuelRate*0.1)*(distance/10)
        remain_distance=(self.fuelRate)/(self.fuelRate*0.1)
        if self.fuelRate==0 :
            self.stop() 

    def stop(self):
        self.velocity=0
        if remain_distance > 0 :
            print('the remain distance = ', remain_distance)
        else:
            print('you arrive the distination')

    