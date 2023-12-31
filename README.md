# Class
classes are the mould for the kind of objects we intend to create.
whenever the class is called, we are creating an object of that class, in fact a class also called data type, where we are having the freedom to add features, types and methods to that data type.

class is definition of the new data type and the object is representation or instantiation of that data type.

## attributes:
the variables used inside a class is called attributes (instance variable).
In object-oriented programming, an attribute is a piece of information or a characteristic associated with an object.
Objects are instances of classes, and classes define the blueprint for objects. 

## methods:

functions inside a class is known as methods.
 
 ## __init__ (instance method):

 it is used to initialize the contents of an object inside a class.

 
 using __ini__ method, we are laying out the foundation of which variables are allowed inside the class (mould), otherwise our class can be messy and others can add their own variables inside our class (blueprint).

in other words we are defining what those attributes can be and cannot be inside our class.

we have more control on what we have created.

as we are adding keys to dictionaries or indexes to arrays, here we are adding variables to our class.

```py

class Details:
    def __init__(self,name, duration):
        self.name = name
        self.duration = duration

def main():
    details = get_info()
    print(f"{details.name} will take {details.duration} months to master. ")
    
def get_info():
    details = Details()
    name = input("Name: ")
    duration = input("Duration: ")
    details = Details(name, duration)
    return details
    
if __name__ == "__main__":
    main()

```


##### Two major steps


1. #### Initialization:
initializes the contents of the object.

```py
 def __init__(self,name, duration):
        self.name = name
        self.duration = duration

# fill the just created empty object with name and duration and save in computer memory.
# self.name and self.duration can be any name, but the naming should be self explanatory.

```


2. #### Constructor call:
it construct an object out of the mould we have made under the class name.
it uses our class as template so that every object have the same structure, but we can customize the contents of the object.

```py
new_object_name = class_name(instance_variables)
```

as the execution starts, when it reaches to instance construction, it will create an empty object inside the computer memory.
when it calls that instance, it will directly move upward and calls __init__ method, and in there using self, the values saved inside the object in computer memory.
we can use any thing instead of self, but it is the convention to use this name. the reason behind having that extra variable(self) is to point to the current object variables that we just created and use it in other place inside the class.


### __str__(self)

if we can an object directly in a function like print, we will see only the address of that object.
if we want see the string representation of our object we can use __str__ instance method.
using self, we are having access to the current object and we can call that object, whenever print(object) is called, it will trigger the __str__(self) method.



### Property

properties are a way to access and manipulate attributes through methods (getter, setter, and deleter methods). 


a property is a special kind of attribute that is accessed like a normal attribute but is implemented using methods known as getter, setter, and deleter.
Properties allow you to define custom behavior for getting, setting, and deleting an attribute. 


the main reason behind using property is to have controlled access to the property of an object.


#### Decorators:

functions that modify or extend the behavior of other functions. 
Decorators are commonly used for tasks like logging, authentication, measuring execution time, and more.

#### Components of property

Usually, we use from three components

1. #### Getter:
   it is responsible for getting value of an attribute
   use py```@property``` decorator to create a read-only property

```py
@property
def subject(self):
    return self._subject
```

2. ### Setter:
   a setter method is responsible for setting value of an attribute
   decorate a method by ```py method_name.setter``` to create a setter for a specific property
   
```py
@subject.setter
def subject(self, value):
    self._subject = value
```

3. ### Deleter:
   a deleter method is responsible for an attribute (a specific information about an object present in the class)
   Decorate a method with py```@<property_name>.deleter``` to create a deleter for a specific property.

    ```py
    @property
    def subject(self):
        del self._subject
    ```

    it is a naming convention that the attribute name and its properties be the same.

## Class Variables and Class methods

1. ### Class Variables: 
   class variables are shared among all instance of a class and can be accessed directly.
   ```py className.classMethod```
   even if we have different objects, but this value will be shared among all of them.


```py

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

```


2. ### Class Methods:
Class methods are methods that are related to the class only and not the instance of the class. They are defined using the @classmethod decorator.



## Inheritance



```py
class Mathematics:
    def __init__(self,name, duration):
        self.duration = duration
        self.name = name
        ...



class ArtificialIntelligence:
    def __init__(self,name, duration):
        self.duration = duration
        self.name = name
        ...
        
class Programming:
    def __init__(self,name, duration):
        self.duration = duration
        self.name = name
        ...


maths = Mathematics("Computation","6 years")
aritificialIntelligence = ArtificialIntelligence("statistics","4 years")
programming = Programming("Logic","6 months")

```

in the above code, Mathematics is the parent class and the other classes are known as child class.
we add in parenthesis the name of the class that the child class is going to inherit and inside the child's init method, we call the parent's init method.
the super() refers to the super or parent class of child class.
we say call the init method of child class.

one thing should be noted is that all the parameters or attributes of the parent class should be present in child class and vice versa, other wise the TypeError will be triggered.



## Operator OverLoading

```py

class Course:
    def __init__(self, name,prerequisite, duration):
        self.name = name
        self.prerequisite = prerequisite
        self.duration = duration
        
    
    def __str__(self):
        return f"{self.name} requires {self.prerequisite} as its prerequisite and it takes {self.duration} months to complete. "
        
machineLearning = Course("Machine learning","Statistics",6)
deepLearning = Course("Deep learning","Calculus",4)

duration = machineLearning.duration + deepLearning.duration
prerequisites = machineLearning.prerequisite + " and " + deepLearning.prerequisite
name = machineLearning.name + " and " + deepLearning.name

print(name)
print(prerequisites)
print(duration)


```


Using operator overloading allowed us to define on common instance method and we can use as many times as we want.

```py 
class Course:
    def __init__(self, name,prerequisite, duration):
        self.name = name
        self.prerequisite = prerequisite
        self.duration = duration
        
    
    def __str__(self):
        return f"{self.name} requires {self.prerequisite} as its prerequisite and it takes {self.duration} months to complete. "
    
    # self refers whatever object on the left and other refers to the object on the right side of + operator.
    def __add__(self, other):
        duration = self.duration + other.duration
        prerequisites = self.prerequisite + " and " + other.prerequisite
        name = self.name + " and " + other.name
        # after object on the left and object on the right together, return one new object with the resulted operations.
        return Course(name,prerequisites,duration)
        
machineLearning = Course("Machine learning","Statistics",6)
deepLearning = Course("Deep learning","Calculus",3)

new_course = machineLearning + deepLearning 
print(new_course)

```