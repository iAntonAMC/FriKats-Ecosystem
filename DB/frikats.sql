.mode column
.headers on
PRAGMA FOREIGN_KEYS = on;

CREATE TABLE customers (
    id_customer INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(150) NOT NULL DEFAULT 'Guest'
);

CREATE TABLE categories (
    id_category INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(150) NOT NULL,
    common_animes VARCHAR(150) NOT NULL
);

CREATE TABLE products (
    id_product INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    product_sku VARCHAR(150) NOT NULL UNIQUE,
    product_name VARCHAR(150) NOT NULL,
    product_description VARCHAR(150) NOT NULL,
    product_price INTEGER NOT NULL CHECK (product_price > 0),
    product_image VARCHAR(150) DEFAULT NULL,
    product_stock INTEGER NOT NULL CHECK (product_stock >= 0),
    id_category INTEGER NOT NULL,
    FOREIGN KEY (id_category) REFERENCES categories(id_category)
);

CREATE TABLE sales (
    id_sale INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    sale_date DATE NOT NULL DEFAULT CURRENT_DATE,
    id_customer INTEGER NOT NULL,
    sale_total INTEGER CHECK (sale_total >= 0) DEFAULT 0,
    FOREIGN KEY (id_customer) REFERENCES customers(id_customer)
);

CREATE TABLE sale_details (
    id_detail INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_sale INTEGER NOT NULL,
    id_product INTEGER NOT NULL,
    total_products INTEGER NOT NULL CHECK (total_products > 0),
    subtotal_price INTEGER NOT NULL CHECK (subtotal_price > 0),
    FOREIGN KEY (id_sale) REFERENCES sales(id_sale),
    FOREIGN KEY (id_product) REFERENCES products(id_product)
);

INSERT INTO customers (customer_name) VALUES ('Guest 1');
INSERT INTO categories (category_name, common_animes) VALUES
    ('Shonnen', 'Naruto, One Piece, Dragon Ball');
INSERT INTO products (product_sku, product_name, product_description, product_price, product_image, product_stock, id_category) VALUES
    ('B01', 'Botón/Pin', 'Fotobotón Metálico', 15, 'ruta/imagen.jpg', 100, 1),
    ('B02', 'Playera', 'Playera Estampada', 100, 'ruta/imagen.jpg', 100, 1),
    ('B03', 'Taza', 'Taza Estampada', 50, 'ruta/imagen.jpg', 100, 1),
    ('B04', 'Llavero', 'Llavero de Acrílico', 30, 'ruta/imagen.jpg', 100, 1),
    ('B05', 'Póster', 'Póster de Papel', 50, 'ruta/imagen.jpg', 100, 1),
    ('B06', 'Mochila', 'Mochila de Tela', 200, 'ruta/imagen.jpg', 100, 1),
    ('B07', 'Figura', 'Figura de Plástico', 150, 'ruta/imagen.jpg', 100, 1);
