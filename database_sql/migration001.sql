-- Initial table creation

-- Users table
CREATE TABLE users (
    user_id   INT          PRIMARY KEY AUTO_INCREMENT,
    username  VARCHAR(30)  UNIQUE NOT NULL,
    password  VARCHAR(100) NOT NULL,
    user_type VARCHAR(10)  NOT NULL
);

-- Items table
CREATE TABLE items (
    item_id   INT  PRIMARY KEY AUTO_INCREMENT,
    item_name TEXT NOT NULL,
    price     INT  NOT NULL
);

-- Orders table
CREATE TABLE orders (
    order_id INT  PRIMARY KEY AUTO_INCREMENT,
    user_id  INT,
    dine_in  BOOLEAN DEFAULT 1,
    notes    TEXT,
    CONSTRAINT FK_User_Order FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);

-- The order items table
CREATE TABLE orders_items (
    order_id INT,
    item_id INT,
    qty INT DEFAULT 1,
    CONSTRAINT FK_Order_OrderItems FOREIGN KEY (order_id)
    REFERENCES orders(order_id),
    CONSTRAINT FK_Item_OrderItems FOREIGN KEY (item_id)
    REFERENCES items(item_id)
);

-- Insert sample data
INSERT INTO users (username, password, user_type) VALUES ("__system", "", "admin"); -- future use
INSERT INTO users (username, password, user_type) VALUES ("default", "", "manager");