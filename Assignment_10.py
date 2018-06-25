#Question 1
class Animal:
     def __init__(self):
         pass
     def animal_attribute(self):
        print("This is an animal class")

class Tiger(Animal):
    def __init__(self,name):
       self.name=name
       print("Tiger")

t=Animal()
t.animal_attribute()
a=Tiger("name")

#Question 2

print("Output of given code is ")
print("A  B")
print("A  B")


#Question 3

class Cop:
    name=input("Enter Name: ")
    age=int(input("Enter age: "))
    work_experience = int(input("Enter work Experience: "))
    designation =input("Enter designation")
    def __init__(self):
        pass
    def add(self):
        place=input("Enter place")
        self.place=place

    def display(self):
            print("name is: ", self.name)
            print("age is: ", self.age)
            print("Work experience is: ", self.work_experience)
            print("designation is: ", self.designation)

    def update(self):
            print("to update the info ")
            name = input("Enter name: ")
            self.name = name
            age = input("enter age")
            self.age = age
            work_experience = input("Enter work Experience")
            self.experience = experience
            designation = input("Enter designation")
            self.designation = designation
            place = input("Enter place")
            self.place = place
            print("updated information is ")
            c.display

class Mission(Cop):
    def add_mission_detail(self):
            pass

c = Cop()
m = Mission()
c.add()
c.display()


#question 4

class Shape:
    length=float(input("Enter length: "))
    breadth=float(input("Enter breadth: "))
    def __init__(self):
        pass
class Rectangle(Shape):
    area=Shape.length*Shape.breadth
    print("Area of Rectagle is: ",area)
class Square(Shape):
    area=Shape.length**2
    print("Area of square is: ",area)
s=Shape()
r=Rectangle()
s=Square

