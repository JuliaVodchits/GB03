import pickle
import os

class Animal():
    def __init__(self, animal_type, name, age):
        self.animal_type = animal_type
        self.name = name
        self.age = age

    def eat(self):
        print(f"Животное {self.name} ест")

    def make_sound(self):
        print(f"{self.animal_type} {self.name} кричит")

    def info(self):
        print(f"Животное: {self.animal_type}, Имя: {self.name}, Возраст: {self.age}")

class Bird(Animal):
    def __init__(self, animal_type, name, age, sound):
        super().__init__(animal_type, name, age)
        self.sound = sound
        
    def eat(self):
        print(f"Птица {self.name} ест")

    def make_sound(self):
        print(f"{self.animal_type} {self.name} кричит {self.sound}")

    def info(self):
        print(f"Птица: {self.animal_type}, Имя: {self.name}, Возраст: {self.age}, Кричит: {self.sound}")
        
class Mammal(Animal):
    def __init__(self, animal_type, name, age, period_of_gestation, sound="", is_overland=True):
        super().__init__(animal_type, name, age)
        self.sound = sound
        self.period_of_gestation = period_of_gestation
        self.is_overland = is_overland

    def eat(self):
        print(f"Млекопитающее {self.name} ест")

    def make_sound(self):
        print(f"{self.animal_type} {self.name} {self.sound}")

    def info(self):
        print(f"Млекопитающее: {self.animal_type}, Имя: {self.name}, Возраст: {self.age}, Кричит: {self.sound}, "  
            f"{'Сухопутное' if self.is_overland else 'Водоплавающее'}, Вынашивает плод: {self.period_of_gestation}")

class Reptile(Animal):
    def __init__(self, animal_type, name, age, is_overland=True):
        super().__init__(animal_type, name, age)
        self.is_overland = is_overland

    def eat(self):
        print(f"Рептилия {self.name} ест")

    def make_sound(self):
        if self.is_overland:
            print(f"{self.animal_type} {self.name} шипит")
        else:
            return None

    def info(self):
        print(f"Рептилия: {self.animal_type}, Имя: {self.name}, Возраст: {self.age}, "
            f"{'Сухопутное' if self.is_overland else 'Водоплавающее'}")


class Employee():
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal):
        animal.eat()

    def awake_animal(self, animal):
        animal.make_sound()

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name)

    def heal_animal(self, animal):
        print(f"{animal.animal_type} {animal.name} выздоравливает")

class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_zoo_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            animal.info()
        print()

    def awake_zoo_animals(self, employee):
        print(f"Животные в зоопарке {self.name} были разбужены сотрудником {employee.name}:")
        for animal in self.animals:
            employee.awake_animal(animal)
        print()

    def feed_zoo_animals(self, employee):
        print(f"Животные в зоопарке {self.name} были накормлены сотрудником {employee.name}:")
        for animal in self.animals:
            employee.feed_animal(animal)
        print()

    def heal_zoo_animals(self, employee):
        print(f"Животные в зоопарке {self.name} были вылечены ветеринаром {employee.name}:")
        for animal in self.animals:
            employee.heal_animal(animal)
        print()

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    def load_from_file(filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        return None


zoo_filename = "zoo_data.pkl"
zoo1 = Zoo.load_from_file(zoo_filename)

if zoo1 is None:
    print("Не удалось загрузить из файла")
    zoo1 = Zoo("Шёнбрун")
    zoo1.add_animal(Bird( "Петух", "Петруша", 1, "кукареку"))
    zoo1.add_animal(Mammal("Коала", "Маруся", 3, "35 дней", "хрюкает"))
    zoo1.add_animal(Mammal("Слон", "Степан", 10, "22 мес.", "трубит"))
    zoo1.add_animal(Mammal("Дельфин", "Тимофей", 9, "12 мес.", "щелкает", False))
    zoo1.add_animal(Reptile("Крокодил", "Геннадий", 20, False))
    zoo1.add_animal(Reptile("Игуана", "Зинаида", 1))

    zoo1.add_employee(ZooKeeper("Петр Петров"))
    zoo1.add_employee(Veterinarian("Марфа Петрова"))

zoo1.view_zoo_animals()
zoo1.awake_zoo_animals(zoo1.employees[0])
zoo1.feed_zoo_animals(zoo1.employees[0])
zoo1.heal_zoo_animals(zoo1.employees[1])

zoo1.save_to_file(zoo_filename)