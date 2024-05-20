from .Product import Product

class Electronics(Product):
    def __init__(self, product_id, product_name, description, price, quantity_in_stock, brand, warranty_period):
        super().__init__(product_id, product_name, description, price, quantity_in_stock, "Electronics")
        self.brand = brand
        self.warranty_period = warranty_period

    # Getters and Setters
    def get_brand(self):
        return self.brand

    def get_warranty_period(self):
        return self.warranty_period

    def set_brand(self, brand):
        self.brand = brand

    def set_warranty_period(self, warranty_period):
        self.warranty_period = warranty_period
