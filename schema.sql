CREATE DATABASE OrderMS
USE OrderMS
-- Create table for Users
CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(10) NOT NULL
);
ALTER TABLE Users
ADD CONSTRAINT CK_Users_role
CHECK(role IN('Admin','User'))

-- Create table for Products
CREATE TABLE Product (
    productId INT PRIMARY KEY,
    productName VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    quantityInStock INT NOT NULL,
    productType VARCHAR(20) NOT NULL
);

ALTER TABLE Product
ADD CONSTRAINT CK_Product_productType
CHECK(productType IN('Electronics','Clothing'))

-- Create table for Electronics
CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    warrantyPeriod INT NOT NULL,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- Create table for Clothing
CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size VARCHAR(10) NOT NULL,
    color VARCHAR(20) NOT NULL,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- Create table for Orders
CREATE TABLE Orders (
    orderId INT PRIMARY KEY IDENTITY(1,1),
    userId INT NOT NULL,
    orderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES Users(userId)
);

-- Create table for OrderDetails
CREATE TABLE OrderDetails (
    orderDetailId INT PRIMARY KEY IDENTITY(101,1),
    orderId INT NOT NULL,
    productId INT NOT NULL,
    FOREIGN KEY (orderId) REFERENCES Orders(orderId),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);