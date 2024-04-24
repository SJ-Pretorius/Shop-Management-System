#-------------------------
#SJ Pretorius  04 May 2023
#-------------------------
from ctuClass import ctuStock
#Initialising the objects
shop1=ctuStock('Default','Default',0,0,0)
shop2=ctuStock('Default','Default',0,0,0)
shop3=ctuStock('Default','Default',0,0,0)
shop4=ctuStock('Default','Default',0,0,0)

#Initialising the lists
itemName=[]
itemPrice=[]
itemStock=[]

#Shop management menu
def manage():
    while True:
        print('''
Shop Management
1. Change shop Name
2. Change shop location
3. Display current shops
4. Display all shops information
0. Back
''')
#Select option
        act=input(f'Select an option: ')
        if act == '0':
            main()
        elif act == '1':
            name()
        elif act == '2':
            location()
        elif act == '3':
            shops()
        elif act == '4':
            info()
        else:
            print()
            print(f'Invalid selection!')

#Change shop name
def name():
    while True:
        print()
        print(f'''Change Shop name

Select Shop
1. {shop1.shopName}
2. {shop2.shopName}
3. {shop3.shopName}
4. {shop4.shopName}
0. Back
''')
#Select shop
        act=input(f'Select an option: ')
        if act == '0':
            manage()
        elif act == '1' or act == '2' or act == '3' or act == '4':
            break
        else:
            print()
            print(f'Invalid selection!')
#Name changing part for shop selected above
    while True:
        name = input(f'Type the new Shop name: ')
        valid = ctuStock.nameCheck(name)
        if valid == 1:
            if act == '1':
                shop1.shopName = name
            elif act == '2':
                shop2.shopName = name
            elif act == '3':
                shop3.shopName = name
            elif act == '4':
                shop4.shopName = name
        else:
            print()
            print(f'Name cannot be blank!')
            continue
        break
    print()
    print(f'Shop name was successfully changed to {name}')

#Change shop location
def location():
    while True:
        print(f'''
Change Shop Location

Select Shop
1. {shop1.shopName}, {shop1.shopLocation}
2. {shop2.shopName}, {shop2.shopLocation}
3. {shop3.shopName}, {shop3.shopLocation}
4. {shop4.shopName}, {shop4.shopLocation}
0. Back''')
#Select shop 
        act=input(f'Select an option: ')
        if act == '0':
            manage()
        elif act == '1' or act == '2' or act == '3' or act == '4':
            break
        else:
            print()
            print(f'Invalid selection!')
#Location changing part for shop selected above
    while True:
        locate=input(f'Enter a location Free State, Gauteng, KZN, Limpopo: ')
        valid = ctuStock.locationCheck(locate)
        if valid == 1:
            if act == '1':
                shop1.shopLocation = locate
            elif act == '2':
                shop2.shopLocation = locate
            elif act == '3':
                shop3.shopLocation = locate
            elif act == '4':
                shop4.shopLocation = locate
            break
        else:
            print()
            print(f'Invalid Location.')
    print()
    print(f'Shop location successfully changed to {locate}')

#Display current shops
def shops():
    print(f'''
Current Shops

1. {shop1.shopName}, {shop1.shopLocation}
2. {shop2.shopName}, {shop2.shopLocation}
3. {shop3.shopName}, {shop3.shopLocation}
4. {shop4.shopName}, {shop4.shopLocation}''')
    input()

#Display all shop information
def info():
    print(f'''
----------------

Shop Name: {shop1.shopName}
Shop Location: {shop1.shopLocation}
Number of Customers: {shop1.customers}
Current Sales: {shop1.sales}
Returns: {shop1.returns}

----------------

----------------

Shop Name: {shop2.shopName}
Shop Location: {shop2.shopLocation}
Number of Customers: {shop2.customers}
Current Sales: {shop2.sales}
Returns: {shop2.returns}

----------------

----------------

Shop Name: {shop3.shopName}
Shop Location: {shop3.shopLocation}
Number of Customers: {shop3.customers}
Current Sales: {shop3.sales}
Returns: {shop3.returns}

----------------

----------------

Shop Name: {shop4.shopName}
Shop Location: {shop4.shopLocation}
Number of Customers: {shop4.customers}
Current Sales: {shop4.sales}
Returns: {shop4.returns}

----------------''')
    input()

#Sales
def sales():
    while True:
        print()
        print(f'Sales')
        for i in range(len(itemName)):
            print(f'{i+1}: {itemName[i]} (R{round(itemPrice[i],2)} per item and {itemStock[i]} in stock)')
        print(f'0. Back')
        print()
#Select item
        sold=input(f'Select an item to be sold: ')
        if sold == '0':
            main()
        elif sold.isdigit():
            if int(sold) <= len(itemName):
                break
            else:
                print()
                print(f'Item number {sold} does not exist!')
        else:
            print()
            print(f'Invalid selection!')
#Input number of items bought
    while True:
        num=input(f'Number of items bought: ')
        if num.isdigit():
            if int(num) <= itemStock[int(sold)-1]:
                break
            else:
                print()
                print(f'Not enough stock!')
        else:
            print()
            print(f'Only numbers!')
#Select shop
    while True:
        loc=input(f'Select a shop (1. {shop1.shopName}, 2. {shop2.shopName}, 3. {shop3.shopName}, 4. {shop4.shopName}): ')
        if loc == '1':
            shop1.customers += 1
            shop1.sales += int(num)
            itemStock[int(sold)-1] -= int(num)
        elif loc == '2':
            shop2.customers += 1
            shop2.sales += int(num)
            itemStock[int(sold)-1] -= int(num)
        elif loc == '3':
            shop3.customers += 1
            shop3.sales += int(num)
            itemStock[int(sold)-1] -= int(num)
        elif loc == '4':
            shop4.customers += 1
            shop4.sales += int(num)
            itemStock[int(sold)-1] -= int(num)
        else:
            print()
            print(f'Invalid location!')
            continue
        break
    print()
    print(f'Sales for shop {loc} successfully recorded!')

#Returns
def returns():
    while True:
        print()
        print(f'Returns')
        for i in range(len(itemName)):
            print(f'{i+1}: {itemName[i]}')
        print(f'0. Back')
        print()
#Select item
        act=input(f'Select an item to return: ')
        if act == '0':
            main()
        elif act.isdigit():
            if int(act) <= len(itemName):
                break
            else:
                print()
                print(f'Item number {act} does not exist!')
        else:
            print()
            print(f'Invalid selection!')
#Input number of items
    while True:
        num=input(f'Number of items to return: ')
        if num.isdigit():
            break
        else:
            print()
            print(f'Only numbers!')
#Select shop
    while True:
        loc=input(f'Select a shop to return to (1. {shop1.shopName}, 2. {shop2.shopName}, 3. {shop3.shopName}, 4. {shop4.shopName}): ')
#Do a bit of math
        if loc == '1':
            shop1.returns += int(num)
            shop1.sales -= int(num)
            itemStock[int(act)-1] += int(num)
        elif loc == '2':
            shop2.returns += int(num)
            shop2.sales -= int(num)
            itemStock[int(act)-1] += int(num)
        elif loc == '3':
            shop3.returns += int(num)
            shop3.sales -= int(num)
            itemStock[int(act)-1] += int(num)
        elif loc == '4':
            shop4.returns += int(num)
            shop4.sales -= int(num)
            itemStock[int(act)-1] += int(num)
        else:
            print()
            print(f'Invalid selection!')
            continue
        break
    print()
    print(f'Item/s successfully returned to shop {loc}!')

#Stocks menu
def stocks():
    while True:
        print(f'''
Stocks
1. Display Stock
2. Add Stock
0. Back
''')
        act=input(f'Select an option: ')
        if act == '0':
            main()
        elif act == '1':
            displayStock()
        elif act == '2':
            addStock()
        else:
            print()
            print(f'Invalid selection!')

#Display stocks
def displayStock():
    print()
    print('Display Stock')
    for i in range(len(itemName)):
        print(f'{i+1}. {itemName[i]}, R{round(itemPrice[i],2)}, {itemStock[i]} available in stock')
    if len(itemName) == 0:
        print()
        print('No Stock!')
    input()

#Add stocks
def addStock():
#Input name for new item and checks if it is not blank
    while True:
        name=input('Enter new item name: ')
        valid = ctuStock.nameCheck(name)
        if valid == 1:
            break
        else:
            print()
            print(f'Name cannot be blank!')
#Input price for new item
    while True:
        price=input('Enter price for new item: R')
        try:
            price = float(price)
            break
        except ValueError:
             print()
             print("Only numbers!")
#Input quantity of item
    while True:
        qt=input('Enter quantity: ')
        if qt.isdigit():
            qt = int(qt)
            break
        else:
            print()
            print(f'Only numbers!')
#Add to lists
    itemName.append(name)
    itemPrice.append(price)
    itemStock.append(qt)
    print()
    print(f'Stock successfully added!')
    main()

#Main menu
def main():
    while True:
        print(f'''
Welcome to CTU Technologies

1. Shop Management
2. Sales
3. Returns
4. Stocks
99. Exit
''')
#Select option
        act=input(f'Select an option or 99 to exit: ')
        if act == '99':
            exit()
        elif act == '1':
            manage()
        elif act == '2':
            sales()
        elif act == '3':
            returns()
        elif act == '4':
            stocks()
        else:
            print(f'Invalid selection!')

main()
