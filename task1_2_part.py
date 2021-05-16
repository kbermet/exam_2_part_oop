class Employee():

    salary_budget = 0
    productivity = 40

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info(self):
        print(f'Employee ID: {self.id}  Lastname: {self.name}')

    def salary(self, salary_flat):
        self.salary_flat = salary_flat
        print(f'Fixed salary is {salary_flat}')
        Employee.salary_budget += self.salary_flat

    def salary_bonus(self, salary_flat, sales):
        self.sales = sales
        self.salary_with_bonus = salary_flat+(50*self.sales)
        print(f'Fixed salary with bonus is {self.salary_with_bonus}')
        Employee.salary_budget += self.salary_with_bonus

    def salary_per_hour(self, hour):
        self.hour=hour
        self.salary_hourly = self.hour*100
        print(f'This month salary is {self.salary_hourly}')
        Employee.salary_budget += self.salary_hourly

    def performance(self, hours):
        self.hours=hours
        print(f'{self.name} productivity is {self.hours} hours.')
        Employee.productivity += self.hours
        if self.hours>=40:
            print(f'This {self.name} is most productive')
        else:
            if self.hours<=20:
                print(f'This {self.name} is least productive')


    def howMany():
        print(f'Total budget for salaries is: {Employee.salary_budget}')

    howMany = staticmethod(howMany)

class Manager(Employee):
    pass

class Secretary(Employee):
    pass

class SalesPerson(Employee):
    pass

class FactoryWorker(Employee):
    pass

class TempSecretary(Employee):
    pass

manager = Manager(1, 'Barsbek Kanatkulov')
manager.info()
manager.salary(45000)
manager.performance(18)
secretary= Secretary(2, 'Alymkul Tilekbaev')
secretary.info()
secretary.salary(20000)
secretary.performance(38)
salesman = SalesPerson(3, 'Aiperi Shalymbekova')
salesman.info()
salesman.salary_bonus(20000, 20)
salesman.performance(18)
factoryman=FactoryWorker(4,'Bakyt Rustamov')
factoryman.info()
factoryman.salary_per_hour(25)
factoryman.performance(25)
factoryman1=FactoryWorker(4,'Bakyt Rustamov')
factoryman1.info()
factoryman1.salary_per_hour(40)
factoryman1.performance(40)
tempsec = TempSecretary(6, 'Zhanar Ryskulov')
tempsec.info()
tempsec.salary_per_hour(33)
tempsec.performance(33)
Employee.howMany()
