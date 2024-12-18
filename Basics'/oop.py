class Animal:
    
    def __init__(self, type):
        self.type = type
        
    def get_type(self):
        return self.type  
    
    def __str__(self):
        return f"This is a {self.type}"  
    
z = Animal('dog')     
    
# print(Animal("Mammal").get_type())
        
# class Crocodile(Animal):
#     def __init__(self):
#         super().__init__(type="Reptile")

# class Snake(Animal):
#     def __init__(self):
#         super().__init__(type="Reptile")
    
# class Dog(Animal):
#     def __init__(self):
#         super().__init__(type="Mammal")
        
# crocodile = Crocodile()  
# snake = Snake()
# dog = Dog()      

# print(crocodile.get_type())
# print(snake.get_type())
print(str(z))

    
       