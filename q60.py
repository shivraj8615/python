class Shape (object):
    sides = None
    def _init_(self, sides) :
            self.sides = sides
            def perimeter (self) :
                perimeter = 0
                for side in self.sides :
                        perimeter += side
                return perimeter
class Triangle(Shape):
       def _init_(self,side1,side2,side3) :
            self.sides = [side1, side2, side3]
class Rectangle(Shape):
      def _init_(self,length,width) :
           self.sides = [length, width, length, width]
class Square(Shape) :
     def _init_(self, side) :
        self.sides = [side, side, side, side]

triangle = Triangle(3, 4, 5)
print("Triangle sides: ", triangle.sides)
print("Perimeter of triangle: ", triangle.perimeter ())
rectangle = Rectangle(4, 2)
print("Rectangle sides: ", rectangle.sides)
print ("Perimeter of rectangle: ", rectangle.perimeter ())
square = Square(2)
print ("Square sides: ", square.sides)
print("Perimeter of square: ", square. perimeter ())