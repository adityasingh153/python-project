#menu
menu = {
    'pizza':500,
    'burger':200,
    'sandwich':100,
    'pasta':300,
    'coffee':50,
    'salad':150,
}
#greet
print("Welcome to the python hotel ")
print("1. pizza 500 \n2. burger 200 \n3. sandwich 100 \n4. pasta 300 \n5. coffee 50 \n6. salad 150")
print("7. exit")

#bill
order_total = 0
item_1 = input("Enter the item you want to order: ")
while item_1 != 'exit':
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your order total is {order_total}")
    else:
        print("Please order something which we can serve !!")
    
    another_order = input("Do you want to order another item? (yes/no): ")
    if another_order.lower() == 'yes':
        item_2 = input("Enter the item you want to order: ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your order total is {order_total}")
        else:
            print("Please order something which we can serve !!")
            print ("Your order total is", order_total)
    else:
        print("Thank you for your order")
        break
