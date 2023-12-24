import random

class Details:
# class variable which will be shared among all methods in the current class.
    courses = ["Artificial Intelligence","Deep learning","Machine learning","Python"]
    
    @classmethod
    def choose(cls,subject):
        return f"{subject} is in {random.choice(cls.courses)}"
        


print()
print("first example")
print(Details.choose("mathematics"))
detail = Details()

print()
print("second example")

class Subjects:
    ai_core = "mathematics"  # Class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Accessing class variable
print(Subjects.ai_core)  # Output: 0

# Creating instances
obj1 = Subjects(1)
obj2 = Subjects(2)

# Modifying class variable
Subjects.ai_core = "statistics"
print(obj1.ai_core) ## statistics
print(obj2.ai_core) ## statistics