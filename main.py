'''class Student:
    print("Hi")

first_student = Student()'''

'''class Student:
    print("Hi")
    def __init__(self):
        seld.height = 160
        print("I am alive!")

first_student = Student()'''

'''class Student:
    def __init__(self):
        self.height = 160
        print(self)

first_student = Student()'''

'''class Student:
    def __init__(self):
        self.height = 160

nick = Student()
print(nick.height)'''

'''class Student:
    def __init__(self):
        self.height = 160
        
nick = Student()
kate = Student(height=170)
print(nick.height)
print(kate.height)'''


'''class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students+=1

nick = Student()
kate = Student(height=170)
print(nick.amount_of_students)
print(kate.amount_of_students)'''


'''class Student:
    def __init__(self):
        print(self.height)
        self.height+=10

nick = Student()
kate = Student()'''

'''x = 10
class Looker:
    # x = 15
    print(x)
    def func_1(self):
        # x = 20
        print(x)
        def func_2():
            # x = 30
        func_2()
some_object = Looker()
some_object.func_1()'''

'''class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students+=1
    def grow(self, height=1):
        self.height+=height
nick = Student()
kate = Student(height=170)
nick.grow(height=15)
print(nick.height)
print(kate.height)'''

'''class Student:
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height

    def __bool__(self):
        return self.name != None

    def __len__(self):
        return self.height

nick = Student("Nick", height=170)
print(nick.__len__())
print(nick.__bool__())
print(len(nick))
print(bool(nick))'''

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.allive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time!")
        self.gladness += 5
        self.progress -= 0.1
    def is_allive(self):
        if self.progress < -0.5:
            print("Casr out...")
            self.allive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.allive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.allive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_allive()

nick = Student(name="Nick")

for day in range(365):
    if nick.allive == False:
        break
    nick.live(day)