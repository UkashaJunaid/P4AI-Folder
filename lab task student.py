class Student:
    def input(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


s1 = Student("ukasha", 19, "BS AI")
s2 = Student("junaidx", 20, "BS CS")

s1.display()
print()
s2.display()