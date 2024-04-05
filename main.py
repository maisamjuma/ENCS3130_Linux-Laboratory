from Admin import Admin
from Product import Product
from Shopper import Shopper

products = []
Shoppers = []
Admins = []

class OnlineStore:
    def __init__(self):
       self.product = []
       self.user = []

    # Implement other methods for admin and shopper actions here
#this function for checking if the user is admin or not
def Admin_only_checking():
        # Ask the user to enter a user ID
    userID = input("Enter your user ID: ")

    # Check if the user ID exists in the list of admins
    admin_user = None
    for admin in Admins:      # Assuming Admin is a list of Admin objects
        if admin.user_id == userID:
            admin_user = admin
            break

    if admin_user is None:
        print("Access denied. User ID does not exist or you are not an admin.")
        return 1


def shopper_admin_checking():
    # Ask the user to enter a user ID
    userID = input("Enter your user ID: ")

    # Check if the user ID exists in the list of shoppers
    shopper_user = None
    for shopper in Shoppers:  # Assuming shopper is a list of Shopper objects
        if shopper.user_id == userID:
            shopper_user = shopper
            break
    admin_user = None
    for admin in Admins:  # Assuming Admin is a list of Admin objects
        if admin.user_id == userID:
            admin_user = admin
            break

    if shopper_user is None and admin_user is None:
        print("Access denied. User ID does not exist or you are not a shopper or admin.")
        return 1


def shopper_only_checking():

        # Ask the user to enter a user ID
        userID = input("Enter your user ID: ")

        # Check if the user ID exists in the list of shoppers
        shopper_user = None
        for shopper in Shoppers:  # Assuming shopper is a list of Shopper objects
            if shopper.user_id == userID:
                shopper_user = shopper
                break

        if shopper_user is None:
            print("Access denied. User ID does not exist or you are not a shopper.")
            return 1




def add_product(): #admin only
    # Implement Add product
    if Admin_only_checking() == 1 :
        return
    print("__________enter the following product information_________")
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    inventory = int(input("Enter product inventory: "))
    supplier = input("Enter product supplier: ")
    has_an_offer = input("Does the product have an offer? (yes/no): ").lower() == "yes"

    if has_an_offer:
            offer_price = float(input("Enter offer price: "))
            valid_until = input("Enter offer valid until (YYYY-MM-DD): ")
    else:
            offer_price = None
            valid_until = None

    product = Product(
            product_id,
            name,
            category,
            price,
            inventory,
            supplier,
            has_an_offer,
            offer_price,
            valid_until
    )
    products.append(product)
    for product in products:
            product.display_product_info()


def place_item_on_sale():
    # Implement Place an item on sale
    if Admin_only_checking() == 1:
        return

    productID= input("Please enter the product id you want to make an offer on :")

    product_item = None

    for product in products: # Assuming shopper is a list of Shopper objects

        if product.product_id == productID:

            product_item = product
            break

    if product_item is None:
        print("____Product does not exist.____")
        return
    for product in products:
        if product.product_id == productID:
            if product.has_offer == '1':
                print("Sorry, this product already has an offer, its valid until: "+ product_item.valid_until)
            else:
                 print("________This product has no offer you can place an offer_______")
                 product.has_offer='1'
                 offer_price = float(input("Enter offer price: "))
                 valid_until = input("Enter offer valid until (YYYY-MM-DD): ")
                 product.offer_price=offer_price
                 product.valid_until=valid_until


    for product in products:
            product.display_product_info()




def update_product():
    # Implement Update product
    if Admin_only_checking() == 1:
        return
    productID = input("Please enter the product id you want to update :")

    product_item = None

    for product in products:

        if product.product_id == productID:
            product_item = product
            break

    if product_item is None:
        print("____Product does not exist.____")
        return
    choice= input("What whould you like to change : 1)product name 2)category 3)product price 4)product inventory 5)product supplier 6)product offer" )
    if choice =='1':
        newNAME=input("Enter the new product name :")
        for product in products:
            if product.product_id == productID:
                product.name=newNAME
    elif choice =='2':
        newCATEGORY = input("Enter the new product category :")
        for product in products:
            if product.product_id == productID:
                product.category=newCATEGORY
    elif choice == '3':
        newPRICE = input("Enter the new product price :")
        for product in products:
            if product.product_id == productID:
                product.price=newPRICE
    elif choice == '4':
        newINVETORY = input("Enter the new product inventory :")
        for product in products:
            if product.product_id == productID:
                product.inventory=newINVETORY
    elif choice == '5':
        newSUPPLIER = input("Enter the new product supplier :")
        for product in products:
            if product.product_id == productID:
                product.supplier=newSUPPLIER
    elif choice == '6':
        newoffer_price = float(input("Enter offer price: "))
        newvalid_until = input("Enter offer valid until (YYYY-MM-DD): ")
        for product in products:
            if product.product_id == productID:
                product.has_offer = '1'
                product.offer_price = newoffer_price
                product.valid_until = newvalid_until
    else :
        print("invalid choice. ")
        return
    for product in products:
            product.display_product_info()

def add_new_user():
    # Implement Add a new user
    if Admin_only_checking() == 1:
        return
    #check if he want to add admin or shopper
    choice=input("do you want to enter a new admin or shopper ?").lower()
    if choice == "admin":
        print("___________please fill the admin information_________")
        user_id = input("Enter admin ID: ")
        name = input("Enter admin name: ")
        date_of_birth = input("Enter admin date of birth (YYYY-MM-DD): ")
        role = int(input("Enter admin role: "))
        active = int(input("Enter the admin activness: "))
        admin = Admin(
            user_id,
            name,
            date_of_birth,
            role,
            active
        )
        Admins.append(admin)
    elif choice == "shopper" :
        print("___________please enter the shopper information_________")
        user_id = input("Enter shopper ID: ")
        name = input("Enter shopper name: ")
        date_of_birth = input("Enter shopper date of birth: ")
        role = int(input("Enter shopper role: "))
        active = int(input("Enter the shopper activness: "))
        shopper = Shopper(
            user_id,
            name,
            date_of_birth,
            role,
            active,
            ready_to_order=0,
        )
        Shoppers.append(shopper)
    else :
        print("_____________________")
        print("please enter admin or shopper for the new user ")
        print("_____________________")
        return
     # Display information for admin users
    for admin in Admins:
            admin.display_user_info()
    # Display information for shopper users
    for shopper in Shoppers:
           shopper.display_user_info()





def update_user():
    # Implement Update user
    if Admin_only_checking() == 1:
        return

def display_all_users():
    # Implement Display all users
    if Admin_only_checking() == 1:
        return

    i=1
    o=1
    for admin in Admins:
        print(f"__________Admin number:{i} information_________")
        admin.display_user_info()
        i+=1
    for shopper in Shoppers:
        print(f"__________shopper number:{o} information_________")
        shopper.display_user_info()
        o+=1

def list_products():
    # Implement List products
    if shopper_admin_checking() == 1:
        return

    choice = input("Please choose what whould you like to see : 1)All products 2)Products with offer 3)Category 4)Name ").lower()
    if choice == "1":
        i=1
        for product in products:
            print(f"_______product {i} information______")
            product.display_product_info()
            i+=1
    elif choice == "2":
        b = 1
        for product in products:
                if product.has_offer == '0':
                    pass
                else:

                    print(f"_______product {b} information______")
                    product.display_product_info()
                    b+=1
    elif choice =="3":
        categoryNAME =input("PLease enter the category name you want to display its product :")
        c = 1
        for product in products:
            if product.category== categoryNAME:

                print(f"_______product {c} information______")
                product.display_product_info()
                c+=1
            else :
                pass
    elif choice =="4":
        NAME =input("PLease enter the name of the product you want to display  :")
        a = 1
        for product in products:
            if product.name == NAME:
                print(f"_______product {a} information______")
                product.display_product_info()
                a+=1
            else :
                pass
    else :
        print("invalid choice, please choose 1-2-3-4")







def list_shoppers():
    # Implement List shoppers
    if Admin_only_checking() == 1:
        return

def add_product_to_basket():
    # Implement Add product to the basket
    if shopper_only_checking() ==1:
        return

def display_basket():
    # Implement Display basket
    if shopper_only_checking() == 1:
        return

def update_basket():
    # Implement Update basket
    if shopper_only_checking() == 1:
        return

def place_order():
    # Implement Place order
    if shopper_only_checking() == 1:
        return

def execute_order():
    # Implement Execute order
    if Admin_only_checking() == 1:
        return

def save_products_to_file():
    # Implement Save products to a file
    if Admin_only_checking() == 1:
        return
    i=1
    save_product_file = input("Enter the name of the file you want to save products in: ")
    try:
        with open(save_product_file, "w") as file:
            # Write the product information to the file
            for product in products:
                file.write(f"_________product {i} information________\n")
                file.write(f"Product ID: {product.product_id}\n")
                file.write(f"Product Name: {product.name}\n")
                file.write(f"Product Category: {product.category}\n")
                file.write(f"Price: {product.price}\n")
                file.write(f"Inventory: {product.inventory}\n")
                file.write(f"Supplier: {product.supplier}\n")
                file.write(f"Has an Offer: {'Yes' if product.has_offer=='1' else 'No'}\n")
                if product.has_offer == '1':
                    file.write(f"Offer Price: {product.offer_price}\n")
                    file.write(f"Valid Until: {product.valid_until}\n")
                file.write("\n")
                i+=1

        print(f"Products saved to '{save_product_file}' successfully.")
    except Exception as e:
        print(f"An error occurred while saving products: {str(e)}")




def save_users_to_text_file():
    # Implement Save users to a text file
    if Admin_only_checking() == 1:
        return

if __name__ == "__main__":
    store = OnlineStore()

   #loading the products
    with open("products.txt", "r") as file:
        for line in file:
            product = Product.from_text(line)
            products.append(product)

    # Example: Print information for all loaded products
    for product in products:
       product.display_product_info()

   #loading the users
    # --------------------------------------------------------------------------



    with open("users.txt", "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace, including the newline character
            data = line.split(";")
            role = int(data[3]) # Assuming role is the 4th element
            if role == 0 :

                Admins.append(Admin(*data))
            else:
                if len(data) > 6:
                    Shoppers.append(Shopper(*data))
                else:
                    Shoppers.append(Shopper(*data))

        # Display information for admin users
       # for admin in Admins:
        #      admin.display_user_info()
    # Display information for shopper users
        #for shopper in Shoppers:
         #  shopper.display_user_info()
    # --------------------------------------------------------------------------------------------

    while True:
        print("\nMenu Options:")
        print("1. Add product (admin-only)")
        print("2. Place an item on sale (admin-only)")
        print("3. Update product (admin-only)")
        print("4. Add a new user (admin-only)")
        print("5. Update user (admin-only)")
        print("6. Display all users (admin-only)")
        print("7. List products (admin and shopper)")
        print("8. List shoppers (admin)")
        print("9. Add product to the basket (shopper-only)")
        print("10. Display basket (shopper-only)")
        print("11. Update basket (shopper-only)")
        print("12. Place order (shopper-only)")
        print("13. Execute order (admin-only)")
        print("14. Save products to a file (admin-only)")
        print("15. Save users to a text file (admin-only)")
        print("16. Exit")

        choice = input("Enter your choice: ")

        menu_actions = {
            '1': add_product,
            '2': place_item_on_sale,
            '3': update_product,
            '4': add_new_user,
            '5': update_user,
            '6': display_all_users,
            '7': list_products,
            '8': list_shoppers,
            '9': add_product_to_basket,
            '10': display_basket,
            '11': update_basket,
            '12': place_order,
            '13': execute_order,
            '14': save_products_to_file,
            '15': save_users_to_text_file,
            '16': lambda: exit("Exiting the system.")
        }

        selected_action = menu_actions.get(choice)
        if selected_action:
            selected_action()
        else:
            print("Invalid choice. Please try again.")
