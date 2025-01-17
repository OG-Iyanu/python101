def birthday_message(name, age):
 message = "Happy Birthday " + name + "! I hear you are " + str(age) + " today!"
 return message

name = "Mark"
age = 40
print(birthday_message(name, age))





def order_drink(size, drink_type):
 order = "You ordered a " + size + " " + drink_type + "."
 return order

size = "large"
drink_type = "chocolate"
print(order_drink(size, drink_type))





def withdraw_cash(pin, balance, pin_attempt, amount):
    if pin_attempt == pin:
        if amount <= balance:
            balance -= amount
            print("Cash is being dispensed...")
            print("New balance:", balance)
        else:
            print("Insufficient funds. Unable to withdraw.")
    else:
        print("Incorrect PIN. Transaction cancelled.")

def main():
    pin = 1234
    balance = 1000

    pin_attempt = int(input("Enter your PIN: "))
    amount = float(input("Enter the amount to withdraw: "))

    withdraw_cash(pin, balance, pin_attempt, amount)
if __name__ == "__main__":
   main()








favorite_sports = ['Football', 'Basketball', 'Tennis', 'Cricket']
print(favorite_sports)

favorite_sports.append('Hockey')
print(favorite_sports)

first_four_elements = favorite_sports[:4]
print(first_four_elements)

fifth_element = favorite_sports[4]
print(fifth_element)

favorite_sports[favorite_sports.index('Hockey')] = 'Ice-Hockey'
print(favorite_sports)

favorite_sports.reverse()
print(favorite_sports)

favorite_sports.sort()
print(favorite_sports)

favorite_sports.pop(favorite_sports.index('Ice-Hockey'))
print(favorite_sports)

favorite_sports.clear()
print(favorite_sports)









import random
def roll_dice():
    return random.randint(1, 6)
def main():
    result = roll_dice()

    if result == 6:
        print("Congrats! Move 2 spaces!")
    else:
        print("Try again!")
if __name__ == "__main__":
    main()





item1 = ('Apple', 0.5, 100)
item2 = ('Banana', 0.3, 150)
item3 = ('Milk', 1.2, 50)
item4 = ('Bread', 1.0, 80)

print("Items in Stock:")
print("1. Name: {}, Price: ${}, Quantity: {}".format(item1[0], item1[1], item1[2]))
print("2. Name: {}, Price: ${}, Quantity: {}".format(item2[0], item2[1], item2[2]))
print("3. Name: {}, Price: ${}, Quantity: {}".format(item3[0], item3[1], item3[2]))
print("4. Name: {}, Price: ${}, Quantity: {}".format(item4[0], item4[1], item4[2]))

total_value = (item1[1] * item1[2]) + (item2[1] * item2[2]) + (item3[1] * item3[2]) + (item4[1] * item4[2])
print("\nTotal Value of Inventory: ${}".format(total_value))

items_to_restock = [item for item in [item1, item2, item3, item4] if item[2] < 10]
if items_to_restock:
    print("\nItems to Restock:")
    for item in items_to_restock:
        print("Name: {}, Quantity: {}".format(item[0], item[2]))
else:
    print("\nAll items are well stocked.")





regular_attendees = {'Alice', 'Bob', 'Charlie'}
vip_attendees = {'David', 'Eva', 'Fiona'}
speakers = {'Grace', 'Henry', 'Isabel'}

regular_attendees.add('John')
vip_attendees.add('Kate')
speakers.add('James')

common_attendees = regular_attendees.intersection(vip_attendees)
print("Common Attendees:", common_attendees)

unique_regular_attendees = regular_attendees.difference(vip_attendees, speakers)
unique_vip_attendees = vip_attendees.difference(regular_attendees, speakers)
unique_speakers = speakers.difference(regular_attendees, vip_attendees)

print("Unique Regular Attendees:", unique_regular_attendees)
print("Unique VIP Attendees:", unique_vip_attendees)
print("Unique Speakers:", unique_speakers)






inventory = {
    'apple': 100,
    'banana': 150,
    'milk': 50,
    'bread': 80
}

inventory['orange'] = 120
inventory['bread'] -= 20

total_quantity = sum(inventory.values())
print("Total Quantity of Products:", total_quantity)

low_stock_items = {product: quantity for product, quantity in inventory.items() if quantity < 50}
print("Low-Stock Items:", low_stock_items)
product_info = inventory.get('banana')
print("Product Information (Banana):", product_info)
