from abc import ABC, abstractmethod

# Step 1: Create an abstract product class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Create concrete products
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle.")

class Square(Shape):
    def draw(self):
        print("Drawing a Square.")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle.")

# Step 3: Create a factory class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "square":
            return Square()
        elif shape_type.lower() == "triangle":
            return Triangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Step 4: Client code
if __name__ == "__main__":
    shapes = ["circle", "square", "triangle"]
    for shape_name in shapes:
        shape = ShapeFactory.get_shape(shape_name)
        shape.draw()
