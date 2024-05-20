import pyodbc
from dao.IOrderManagementRepository import IOrderManagementRepository
from entity.Product import Product
from entity.Electronics import Electronics
from entity.User import User
from exception.InvalidUserException import InvalidUserException
from exception.UserNotFoundException import UserNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
from util.DBConnUtil import DBConnUtil

class OrderProcessor(IOrderManagementRepository, DBConnUtil):
    def login(self, username, password):
        self.cursor.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
        user_data = self.cursor.fetchone()
        if not user_data:
            raise UserNotFoundException("Invalid username or password")
        
        user_id, username, password, role = user_data
        return User(user_id, username, password, role)

    def create_order(self, user, products):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM Users WHERE userId = ?", user.get_user_id())
            user_count = self.cursor.fetchone()[0]
            if user_count == 0:
                self.cursor.execute("INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                user.get_user_id(), user.get_username(), user.get_password(), user.get_role())
                self.conn.commit()
                print("User created successfully.")
                    
            self.cursor.execute("INSERT INTO [Orders] ( UserId) OUTPUT INSERTED.OrderId VALUES (?)", user.get_user_id())
            order_id = self.cursor.fetchone()[0]
            print(order_id)
            order_product_data = [(order_id, product.get_product_id()) for product in products]
            self.cursor.executemany("INSERT INTO OrderDetails (OrderId, ProductId) VALUES (?, ?)", order_product_data)
            self.conn.commit()
            print("Order created successfully.")
        except Exception as e:
            print("Error creating order:", e)
        
    def cancel_order(self, userId, orderId):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM Users WHERE userId = ?", userId)
            user_count = self.cursor.fetchone()[0]
            if user_count == 0:
                raise UserNotFoundException(f"User with ID {userId} not found.")

            self.cursor.execute("SELECT COUNT(*) FROM [Orders] WHERE userId = ? AND orderId = ?", userId, orderId)
            order_count = self.cursor.fetchone()[0]
            if order_count == 0:
                raise OrderNotFoundException(f"Order with ID {orderId} not found for user {userId}.")
            self.cursor.execute("DELETE FROM [OrderDetails] WHERE orderId = ?", orderId)
            self.cursor.execute("DELETE FROM [Orders] WHERE userId = ? AND orderId = ?", userId, orderId)
            self.conn.commit()
            print("Order cancelled successfully.")

        except UserNotFoundException as e:
            print("Error cancelling order:", e)
        except OrderNotFoundException as e:
            print("Error cancelling order:", e)
        except Exception as e:
            print("Error cancelling order:", e)

    def create_product(self, user, product):
        # if user.role.lower() != "admin":
        #     raise InvalidUserException("Only admins can create products")
        
        self.cursor.execute(
            "INSERT INTO Product (productId, productName, description, price, quantityInStock, productType) VALUES (?,?,?,?,?,?)",
            (
                product.product_id,
                product.product_name,
                product.description,
                product.price,
                product.quantity_in_stock,
                product.product_type,
            ),
        )
        if product.product_type.lower() == 'electronics':
            self.cursor.execute(
                "INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES (?, ?, ?)",
                (
                    product.product_id,
                    product.brand,
                    product.warranty_period
                ),
            )
        elif product.product_type.lower() == 'clothing':
            self.cursor.execute(
                "INSERT INTO Clothing (productId, size, color) VALUES (?, ?, ?)",
                (
                    product.product_id,
                    product.size,
                    product.color
                ),
            )
        self.conn.commit()

    def create_user(self, user):
        self.cursor.execute(
            "INSERT INTO Users (userId, username, password, role) VALUES (?,?,?,?)",
            (user.user_id, user.username, user.password, user.role),
        )
        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM Product")
        products = self.cursor.fetchall()
        return products
    
    def get_products_by_id(self, product_id):
        self.cursor.execute("SELECT * FROM Product WHERE productId = ?", (product_id,))
        product = self.cursor.fetchone()
        return product

    def get_order_by_user(self, user):
        self.cursor.execute("SELECT * FROM Users WHERE username=?", (user.username,))
        user_data = self.cursor.fetchone()
        
        if not user_data:
            raise UserNotFoundException("User not found")
        
        self.cursor.execute("SELECT * FROM Orders WHERE userId=?", (user.user_id,))
        orders = self.cursor.fetchall()
        return orders
