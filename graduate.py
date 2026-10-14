class Graduate(Student):
    def init(self, name, age, course, research_topic):
        super()._init_(name, age, course)
        self.research_topic = research_topic

    def display(self):
        super().display()
        print("Research Topic:", self.research_topic)


g1 = Graduate("Mubashir", 19, "BS AI", "Artificial Intelligence")

g1.display()