class Shapes:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"I am a {self.name}.")

class Polygon(Shapes):
    def __init__(self,name,sides,right_angles,acute_angles,obtuse_angles,reflex_angles):
        super().__init__(name)
        self.sides = sides
        self.right_angles = right_angles
        self.acute_angles = acute_angles
        self.obtuse_angles = obtuse_angles
        self.reflex_angles = reflex_angles
    
    def show_details(self):
        print("The details of this shape are: ")
        print(f"Name: {self.name}")
        print(f"Sides: {self.sides}")
        print(f"Right_angles: {self.right_angles}")
        print(f"Acute_angles: {self.acute_angles}")        
        print(f"Obtuse_angles: {self.obtuse_angles}")
        print(f"Reflex_angles: {self.reflex_angles}")

polygon1 = Polygon("Square",4,4,0,0,0)
polygon2 = Polygon("Parallelogram",4,0,2,2,0)
polygon3 = Polygon("Arrowhead",4,0,3,0,1)
polygon4 = Polygon("Isosceles Trapezium",4,0,2,2,0)

polygon1.greet()
polygon1.show_details()

polygon2.greet()
polygon2.show_details()

polygon3.greet()
polygon3.show_details()

polygon4.greet()
polygon4.show_details()