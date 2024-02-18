class MyClass:
    def sum(self, x, y=None):  # Method with default parameter
        if y is None:
            return x
        else:
            return x + y

# Create an instance of the class
obj = MyClass()

# Call the method with one argument
result1 = obj.sum(2)
print("Result 1:", result1)  # Output: 2

# Call the method with two arguments
result2 = obj.sum(1, 2)
print("Result 2:", result2)  # Output: 3
