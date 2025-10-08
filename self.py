class human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f"hi, my name is {self.name}, my age is {self.age} years old and im {self.gender}")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

ryan = human("ryan", 18, "male")

ryan.speak()
ryan.eat()
ryan.sleep()
