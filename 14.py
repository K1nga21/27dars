class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Mablag' musbat bo'lishi kerak.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Mablag' yetarli emas yoki manfiy miqdor.")

    def get_balance(self):
        return self.__balance  # Agar balansni ko'rsatish mumkin bo'lsa

class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary, is_manager=False):
        if is_manager:
            self.__salary = new_salary
        else:
            raise PermissionError("Faqat menejerlar maoshni yangilay oladi.")

person = Person("Otabek", 23)
print(person.get_name())  # Ali
print(person.get_age())

account = Account(100000)
account.deposit(5500)
account.withdraw(30)

print(account.get_balance())  # 120


employee = Employee("Shaydo", "Menejer", 3000000)
print(employee.get_name())
print(employee.get_salary())
employee.set_salary(3500000, is_manager=True)
print(employee.get_salary())
