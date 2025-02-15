CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),  
    last_name VARCHAR(100),   
    gender VARCHAR(10),       
    DOB DATE,                 
    job_title VARCHAR(100),   
    job_industry_category VARCHAR(100), 
    deceased_indicator BOOLEAN, 
    wealth_segment VARCHAR(50), 
    owns_car BOOLEAN,          
    address VARCHAR(255),       
    postcode INTEGER,           
    state VARCHAR(50),          
    country VARCHAR(50),        
    property_valuation INTEGER  
);

CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    brand VARCHAR(100),  
    product_line VARCHAR(100),  
    product_class VARCHAR(100),  
    product_size VARCHAR(50),  
    list_price FLOAT,  
    standard_cost FLOAT  
);

CREATE TABLE transaction (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,  
    product_id INTEGER NOT NULL,   
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    online_order BOOLEAN DEFAULT FALSE,  
    order_status VARCHAR(50)
);




INSERT INTO product (product_id, brand, product_line, product_class, product_size, list_price, standard_cost)
SELECT DISTINCT product_id, brand, product_line, product_class, product_size, list_price, standard_cost
FROM temp_table
ON CONFLICT (product_id) DO NOTHING;