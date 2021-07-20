grocery_item = {} # defines empty dictionary

grocery_history = [] # defines empty list


stop = 'go'

while stop != 'q' : # creates the while loop

    item_name = input('Item name: ') # accepts the item name

    quantity = input('Quantity purchased: ') # accepts quantity of items purchased

    cost = input('Price per item: ') # accepts price per item

    grocery_item['name'] = item_name
    grocery_item['number'] = int(quantity)
    grocery_item['price'] = float(cost) # creates each variablefor the dictionary

    grocery_history.append(grocery_item.copy()) # adds grocery items to the list
    
    stop = input("Would you like to enter another item? \nType 'c' for continue or 'q' to quit: ") # creates input for user to continue or stop their grocery list


grand_total = 0 # creates the grand total variable
  

for index, item in enumerate(grocery_history): # creates the for loop
  

  item_total = item['number'] * item['price']  # creates the equation for the price of x number of items

  grand_total += item_total # adds our item prices to our grand total

  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total)) # outputs the user inputs into the grocery list
  
  
  item_total = 0 # sets the initial item total to 0 with no inputs

print('Grand total: $%.2f' % grand_total) # prints the grand total of all inputs
