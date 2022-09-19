import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='grocerymart'
)

mycursor = mydb.cursor()

print('Hello User, Welcome to MyGroceryMart')
mycursor.execute('select locality_name from locality')
locality_list = mycursor.fetchall()
mycursor.reset()

locality_name = []
print([locality for locality in locality_list])

locality_selected = input('Please select your Locality: ')

locality_name.append(locality_selected)
print(locality_name,type(locality_name))

locality_id = "SELECT locality_name FROM locality WHERE locality_id = %s"
mycursor.execute(locality_id, locality_name)
# mycursor.reset()
locality_id_vendor = mycursor.fetchall()
locality_id_int = [locality_name for locality_name in locality_id_vendor]
print(locality_id_int,type(locality_id_int))

mycursor.execute('select category_name from category')
category_list = mycursor.fetchall()
category_name = []
print([category for category in category_list])
mycursor.reset()


category_selected = input('Please select from our range of categories: ')

category_name.append(category_selected)
print(category_name)

category_id = "select product_name ,product_price from products where category_id=%s"
mycursor.execute(category_id, category_name)

product_list = mycursor.fetchall()
print([product for product in product_list])
mycursor.reset()



user_product_limit_v = True
cart = []

while(user_product_limit_v):
    product_selected = []
    user_product_selected = input('Select Product from List: ')
    product_selected.append(user_product_selected)
    user_product_quantity = input('Please select product quantity:')
    user_product_price = "Select product_price from products where product_name=%s"
    mycursor.execute(user_product_price, product_selected)
    product_price_ex = mycursor.fetchall()
    p_price = product_price_ex[0]
    # print(p_price, type(p_price))
    p_price_int = int(p_price[0])
    print(p_price_int,type(p_price_int))
    product_dict = {
        "product_name": user_product_selected,
        "product_price": p_price_int,
        "product_quantity": user_product_quantity
    }
    cart.append(product_dict)
    user_product_limit = input("Do you want to add more Products to Cart: Type Y for Yes or N for No")

    # TODO: Fetch Details from Product Table
    # TODO: Create Dictionary for the Product details fetched
    # TODO: Append created dictionary to a List
    if user_product_limit == 'Y':
        user_product_limit_v = True
    else:
        user_product_limit_v = False

print('Your Cart: ', cart)


def calculate_price(cart):
    total_cart_value = 0
    for products in cart:
        total_cart_value += products['product_price'] * float(products['product_quantity'])
    print('Total Cart Price: ', total_cart_value)


calculate_price(cart)


# TODO Generate Bill and Fetch the nearest Store; Select the nearest Store and deduct Stock from that Store where the purchase is made

mycursor.reset()


res = [int(x) for x in str(locality_selected)]


vendor_name=('select vendor_id from vendor where vendor_locality=%s')
mycursor.execute(vendor_name,res)
vendor_locality_list = mycursor.fetchall()

vendor_list=[vendor for vendor in vendor_locality_list]
print(vendor_list,type(vendor_list))

mycursor.reset()
res1 = [int(x) for x in str(vendor_list)]
def max_stock(cart,vendor_list,res1):
    for products in cart:
        max_stock_vendor=('SELECT MAX(product_stock) FROM Stock WHERE product_vendor = "%s" AND product_id = "%s"')
        mycursor.execute(max_stock_vendor,res1,user_product_selected)
        max_stock_vendor_list = mycursor.fetchall()

        print([stock for stock in max_stock_vendor_list])


max_stock(cart,vendor_list)