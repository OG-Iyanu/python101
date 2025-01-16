def birthday_message(name, age):
    message = "Happy Birthday " + name + "! I hear you are " + str(age) + " today!"
    return message
name = "Jane"
age = 22
print(birthday_message(name, age))




def order_drink(size, drink_type):
#Generate a drink order.
    order = "You ordered a " + size + " " + drink_type + "."
    return order
# Example usage:
size = "medium"
drink_type = "latte"
print(order_drink(size, drink_type))




'''def size_drink(size, drink_type):
    ordered = "you ordered a "+ size +" "drink_type+"."
    return ordered
size = "medium"
drink_type = "chocolate"
print(ordered(size, drink_typetype))'''