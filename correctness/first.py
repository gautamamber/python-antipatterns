# Accessing protected member from outside the class using  (_) is a bad practice or antipattern

# Example of anti-pattern

class Rectangle(object):
    def __init__(self, width, height):
        # protected members
        self._width = width
        self._height = height

r = Rectangle(3,4)
print("Width is {} ".format(r._width))

# If you want to access the protected member outside class make sure, it does not cause any trouble
# Refactor it such that it becomes a part of public interface of class