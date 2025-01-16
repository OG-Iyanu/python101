class Rectangle:

    def __init__ (self, width, height):
        self.__width = width
        self.__height = height


    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def set_width(self, new_width):
        self.__width = new_width

    def set_height(self, new_height):
        self.__height = new_height

new_rectangle = Rectangle(10,8)

new_rectangle.set_width(44)
new_rectangle.set_height(22)
print(new_rectangle.get_width.get_height())
print