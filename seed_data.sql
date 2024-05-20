-- Insert sample data into Users table
INSERT INTO Users (userId, username, password, role) VALUES 
(1, 'admin1', 'password1', 'Admin'),
(2, 'user1', 'password2', 'User'),
(3, 'user2', 'password3', 'User'),
(4, 'admin2', 'password4', 'Admin'),
(5, 'user3', 'password5', 'User'),
(6, 'user4', 'password6', 'User'),
(7, 'admin3', 'password7', 'Admin'),
(8, 'user5', 'password8', 'User'),
(9, 'user6', 'password9', 'User'),
(10, 'admin4', 'password10', 'Admin');

-- Insert sample data into Product table
INSERT INTO Product (productId, productName, description, price, quantityInStock, productType) VALUES
(1, 'Smartphone', 'Latest model', 6990.99, 50, 'Electronics'),
(2, 'Laptop', 'High performance', 1199.99, 30, 'Electronics'),
(3, 'Tablet', 'Lightweight and powerful', 4999.99, 100, 'Electronics'),
(4, 'Smartwatch', 'Advanced features', 1909.99, 75, 'Electronics'),
(5, 'T-shirt', 'Cotton, comfortable', 1909.99, 200, 'Clothing'),
(6, 'Jeans', 'Denim, regular fit', 1049.99, 150, 'Clothing'),
(7, 'Jacket', 'Leather, stylish', 1099.99, 60, 'Clothing'),
(8, 'Sneakers', 'Running shoes', 1059.99, 120, 'Clothing'),
(9, 'Headphones', 'Noise-cancelling', 1229.99, 80, 'Electronics'),
(10, 'Dress', 'Elegant evening dress', 3489.99, 40, 'Clothing');

-- Insert sample data into Electronics table
INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES
(1, 'BrandA', 24),
(2, 'BrandB', 36),
(3, 'BrandC', 12),
(4, 'BrandD', 18),
(9, 'BrandE', 24);

-- Insert sample data into Clothing table
INSERT INTO Clothing (productId, size, color) VALUES
(5, 'M', 'Red'),
(6, 'L', 'Blue'),
(7, 'XL', 'Black'),
(8, '10', 'White'),
(10, 'S', 'Green');

