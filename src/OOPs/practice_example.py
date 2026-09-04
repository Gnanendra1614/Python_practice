class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print("Brand:",self.brand)
        print("Color:",self.color)
        
        
car1=Car("BMW","White")
car1.display()