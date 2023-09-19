class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    def __init__(self, width, height):
        self.width = width
        self.height = height



    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"
   
    def verify_input(self):
        if self.width > 0 and self.height > 0:
            return True
        else:
            return False

    def area(self):
        if not self.verify_input():
            return "Invalid input"
        else:
            return self.width * self.height

    def perimeter(self):
        if not self.verify_input():
            return "Invalid input"
        else: 
            return (2 * self.width) + (2 * self.height)
    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()