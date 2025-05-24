from functions import add_numbers, greet, square_number, is_even
from classes import Car, Student, BankAccount


sum_result = add_numbers(3, 5)
greeting_message = greet("Alice")
square_result = square_number(4)
even_check = is_even(10)


print(sum_result)        
print(greeting_message)   
print(square_result)     
print(even_check)       


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

student1 = Student("Bob", 20)
student2 = Student("Emma", 22)

account1 = BankAccount("John Doe", 500)


print(car1.get_details())       
print(car2.get_details())       
print(Car.get_total_cars())     

print(student1.get_info())      
print(student2.get_info())     
print(Student.get_total_students()) 

print(account1.deposit(200))    
print(account1.withdraw(100))    
print(BankAccount.bank_name)    