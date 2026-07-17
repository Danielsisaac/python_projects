products = [['Apple', 1.2], ['Orange', 0.8], ['Banana', 2.0]]
print ('''

Welcome to the Dan Digital Mart
The available products are:
1. Apple at 1.2
2. Orange at 0.8
3. Banana at 2.0

You're welcome. We're happy to be of service''')

while True:
    user_index_input = input("Enter the item index (1-3) you want to get (or done, when all the items you want have been gotten): ")
    if user_index_input.lower() == "done":
        break
    if user_index_input():
        index_input = int(user_index_input)
        break
    elif int(user_index_input) > 3:
        print ("Invalid input: Please ensure that your input is in line with the indexed number of products")
    else:
        print ("Invalid input: Please ensure that your input is a digit no more than the number of indexed available products listed")
    list_index = int(index_input) - 1
    selected_item = products[list_index]
    product_name = selected_item[0]
    product_price = selected_item[1]

    while True:
        user_amount_input = input("Enter the quantity of the product you want to get (using only numbers): ")
    if user_amount_input():
        quantity = int(user-amount_input)
        break
    else:
        print ("Invalid input: Please input the quantity of the product you want to get in digits")
    
    item_total = product_price * quantity
    total_cost += item_total

    print (selected_item, quantity)
    print (item_total, total_cost)


# print ("Store receipt", "Apple\t1.2", sep="\n")
# print ("Total:", Mul, sep="\t", end="\n")
# print ("Come back next time")
