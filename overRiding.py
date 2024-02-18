class Physics:
    def at_your_core(self):
        return "Explaining Universe"

class Maths(Physics):
    def at_your_core(self):
        return "Universe Language"

class Programming(Maths):
    def at_your_core(self):
        return "Logic"

# Creating instances of Physics, Maths, and Programming.
physics = Physics()
maths = Maths()
programming = Programming()
# Calling overridden methods
print(physics.at_your_core())  # Output: Explaining Universe
print(maths.at_your_core())  # Output: Universe Language
print(programming.at_your_core())  # Output: Logic
