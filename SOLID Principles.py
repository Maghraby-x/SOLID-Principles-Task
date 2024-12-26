from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class BonusCalculator(ABC):  
    @abstractmethod
    def calculate_bonus(self, salary):
        pass
   
    

class FixedBonus(BonusCalculator):
    def calculate_bonus(self, salary):
        return 500  

class PercentageBonus(BonusCalculator):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_bonus(self, salary):
        return salary * self.percentage / 100
    
    


class PayProcessor(ABC): 
    @abstractmethod
    def process_payment(self, employee_name, amount):
        pass
    

class BankTransfer(PayProcessor):
    def process_payment(self, employee_name, amount):
        print(f"Transferring ${amount:.2f} to {employee_name}'s bank account.")
 
 
class Payroll:
    def __init__(self, bonus_calculator: BonusCalculator, pay_processor: PayProcessor):
        self.bonus_calculator = bonus_calculator
        self.pay_processor = pay_processor

    def pay_employee(self, employee: Employee):
        bonus = self.bonus_calculator.calculate_bonus(employee.salary)
        total_payment = employee.salary + bonus
        self.pay_processor.process_payment(employee.name, total_payment)
