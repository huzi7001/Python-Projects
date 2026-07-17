menu = {"HOT BEVREGES":
{"Espresso": 300,
"Americano": 350,
"Cappuccino": 450,
"Latte (Vanilla)" : 500,
"Latte (Caramel)" : 500,
"Latte (Hazelnut)" : 500,
"Latte (Almond)" : 500,
"Mocha" :550,
"Macchiato" : 400,
"Flat White" : 450,
"Chai Latte" : 400,
"Hot Chocolate" : 500,
"Matcha Green Tea" : 600},

"COLD BEVREGES" :
{"Iced Coffee (Black)":300,
"Iced Coffee (Latte)":300,
"Iced Coffee (Mocha)":300,
"Cold Brew Coffee": 400,
"Iced Tea (Lemon, Peach, Green)": 300,
"Milkshakes (Chocolate, Strawberry, Oreo, Banana)": 450,
"Smoothies (Berry Blast, Mango, Avocado, Green Detox)": 500,
"Fresh Lemonade": 280,
"Iced Matcha Latte": 550,
"Frappe (Coffee)": 480,
"Coconut Water": 220,
"Kombucha": 600},

"PASTRIES AND BAKERY": 
        {"Croissant (Plain)": 300,
        "Croissant (Almond)": 350,
        "Croissant (Chocolate)": 380,
        "Muffin (Blueberry)": 280,
        "Muffin (Chocolate)": 300,
        "Danish Pastry": 320,
        "Cinnamon Roll": 350,
        "Scone (Raisin)": 280,
        "Scone with Cream Cheese": 400,
        "Brownie": 350,
        "Cheesecake Slice": 500,
        "Doughnut (Glazed)": 250},
    
"SANDWICHES AND LIGHT BITES":
        {"Classic Club Sandwich": 550,
        "Grilled Cheese Sandwich": 450,
        "Tuna Melt Sandwich": 500,
        "Egg & Avocado Toast": 480,
        "BLT Sandwich (Bacon, Lettuce, Tomato)": 550,
        "Caprese Sandwich": 500,
        "Turkey & Swiss Sandwich": 600,
        "Ham & Cheese Croissant": 580,
        "Veggie Wrap": 480,
        "Chicken Pesto Panini": 650},
    
"DESSERTS AND SWEET TREETS": {
        "Tiramisu": 600,
        "Chocolate Lava Cake": 650,
        "Apple Pie": 500,
        "Red Velvet Cake Slice": 550,
        "Ice Cream (1 Scoop)": 250,
        "Ice Cream (2 Scoops)": 400,
        "Eclairs": 380,
        "Waffles with Maple Syrup": 500,
        "Panna Cotta": 550,
        "Churros with Chocolate Dip": 450,
        "Crepes (Nutella)": 600,
        "Crepes(Strawberry)": 600}}

# MENU DISPLAY
print ("\nWELCOME TO OUR CAFE!")
for i,j in menu.items():
    print(f"\n\t{i}")
    for k,l in j.items():
        print(f"{k}: Rs.{l}")

# PROCESSING ORDER
order = []
amount = []
while True:
    o = input("\nEnter Item you want or type 'done' to finish: ").capitalize()

    if o == "Done":
        break  # Exit the loop

    item_found = False
    for i, j in menu.items():
        for k, l in j.items():
            if o in k.capitalize():
                order.append(f"{k}")
                amount.append(f"{l}")
                item_found = True
                break  # Break out of the inner loop if  item is found
        if item_found:
            break  # Break out of the outer loop if item is found

    if not item_found:
        print("Item not Available.\n Please try again.") # Display error message if item not found and continue the loop

# DISPLAY FINAL ORDER  
print(f"\nYour order is:\n")
i = 1
for item in order:     # Display the items of  order in diferent lines 
    print(f"{i}- {item}")
    i += 1

# BILL DISPLAY
print ("\n    BILL")
print("BILL SUMMARY:")
bill_summary = []
for i in range (len(order)):
    bill_summary.append(f"{order[i]} : Rs.{amount[i]}")
        
for item in bill_summary:
    print(f"    {item}")    # print bill summary
    
# TOTAL BILL
print ("TOTAL BILL:")
total_cost = 0    
for a in amount:   
      total_cost += int(a)  
print(f"    your total bill is Rs.{total_cost}")

