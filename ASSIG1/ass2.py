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
    employees = [] #list of objects of employee
    employeesNum= len(employees)

    def __init__(self, name='itiMans'):
        self.name = name 
        
         
         
    
    def get_all_employees(self):
        for i in employees :
            print('id : ', i.id , ',' , 'name : ', i.name) 
        
    def  get_employee(self,empId):
        for i in employees :
            if i.id == empId :
                print('id : ', i.id , ',' , 'name : ', i.name) 
            else :
                print('no employee has that id')
        

    def hire(self,Employee):
       self.employees.append(employee)  
       self.employeesNum=self.employeesNum+1

    def fire (self,empId):
        for i in employees :
            if i.id == empId :
                self.employees.remove(i)
                self.employeesNum=self.employeesNum-1
            else :
                print('no employee has that id')

        
    @staticmethod  
    def calculate_lateness(self,targetHour=9 , moveHour, distance, velocity):
        time=distance/velocity
        if targetHour-moveHour > time:
            return 'late'
        else :
            return 'not late'
       
    def check_lateness (self, empId, moveHour):
        for i in employees :
            if i.id == empId :
                check=Office.calculate_lateness(moveHour,i.distanceToWork,i.empCar.velocity)
                if check == 'late':
                    i.salary=i.salary-10
                else :
                    i.salary=i.salary+10 
            else :
                print('no employee has that id')


    def deduct(self,empId, deduction):
       for i in employees :
            if i.id == empId :
                i.salary=i.salary-deduction
            else :
                print('no employee has that id') 
       

    def reward(self,empId, reward):
        for i in employees :
            if i.id == empId :
                i.salary=i.salary+reward
            else :
                print('no employee has that id')
    
    def change_emps_num (self, num):
        self.employeesNum=num
        len(self.employees)=num

    
       
       


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

    