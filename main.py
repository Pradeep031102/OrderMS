from dao.OrderProcessor import OrderProcessor
from entity.Product import Product
from entity.User import User
from entity.Electronics import Electronics
from entity.Clothing import Clothing
from exception.InvalidUserException import InvalidUserException
from exception.UserNotFoundException import UserNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException

def main():
    order_processor = OrderProcessor()
    current_user = None

    while True:
        if current_user is None:
            print("\nLogin/Register:")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                try:
                    current_user = order_processor.login(username, password)
                    print(f"Login successful. Welcome {current_user.get_username()}!")
                except UserNotFoundException as e:
                    print(f"Error: {e}")
            elif choice == 2:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")
                user = User(user_id, username, password, role)
                order_processor.create_user(user)
                print("User registered successfully. Please login.")
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("\nMenu:")
            print("1. Create User")
            print("2. Create Product")
            print("3. Create Order")
            print("4. Cancel Order")
            print("5. Get All Products")
            print("6. Get Orders by User")
            print("7. Logout")
            print("8. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if current_user.get_role().lower() != "admin":
                    print("Only admins can create users.")
                    continue
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")
                user = User(user_id, username, password, role)
                order_processor.create_user(user)
                print("User created successfully.")

            elif choice == 2:
                if current_user.get_role().lower() != "admin":
                    print("Only admins can create products")
                    continue
                product_id = int(input("Enter Product ID: "))
                product_name = input("Enter Product Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                quantity_in_stock = int(input("Enter Quantity in Stock: "))
                product_type = input("Enter Product Type (Electronics/Clothing): ")

                if product_type.lower() == "electronics":
                    brand = input("Enter Brand: ")
                    warranty_period = int(input("Enter Warranty Period: "))
                    product = Electronics(product_id, product_name, description, price, quantity_in_stock, brand, warranty_period)
                elif product_type.lower() == "clothing":
                    size = input("Enter Size: ")
                    color = input("Enter Color: ")
                    product = Clothing(product_id, product_name, description, price, quantity_in_stock, size, color)
                else:
                    print("Invalid product type.")
                    continue

                try:
                    order_processor.create_product(current_user, product)
                    print("Product created successfully.")
                except InvalidUserException as e:
                    print(f"Error: {e}")
                
            elif choice == 3:
                try:
                    userId = int(input("Enter User ID: "))
                    products = []
                    while True:
                        productId = int(input("Enter Product ID (0 to finish): "))
                        if productId == 0:
                            break
                        products.append(Product(productId, None, None, None, None, None))
                    user = User(userId, None, None, None)
                    order_processor.create_order(user, products)
                    print("Product Order Successfully done.")
                except UserNotFoundException as e:
                    print(f"Error: {e}")

            elif choice == 4:
                userId = int(input("Enter User ID: "))
                orderId = int(input("Enter Order ID: "))
                try:
                    order_processor.cancel_order(userId, orderId)
                except UserNotFoundException as e:
                    print("User not found:", e)
                except OrderNotFoundException as e:
                    print("Order not found:", e)
                except Exception as e:
                    print("An error occurred:", e)

            elif choice == 5:
                products = order_processor.get_all_products()
                for product in products:
                    print(product)

            elif choice == 6:
                try:
                    orders = order_processor.get_order_by_user(current_user)
                    for order in orders:
                        print(order)
                except UserNotFoundException as e:
                    print(f"Error: {e}")

            elif choice == 7:
                current_user = None
                print("Logged out successfully.")

            elif choice == 8:
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
