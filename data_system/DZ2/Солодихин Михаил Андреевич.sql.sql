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


CREATE TABLE transaction (
	transaction_id SERIAL PRIMARY key, 
	product_id INTEGER,
	customer_id INTEGER,
	transaction_date DATE,
	online_order BOOLEAN,
	order_status VARCHAR(100),
	brand VARCHAR(100),
	product_line VARCHAR(100),
	product_class VARCHAR(100),
	product_size VARCHAR(100),
	list_price FLOAT,
	standard_cost FLOAT
);


SELECT DISTINCT brand
FROM transaction
WHERE standard_cost > 1500;

SELECT * 
FROM transaction
WHERE order_status = 'Approved'
AND transaction_date BETWEEN '2017-04-01' AND '2017-04-09';

SELECT DISTINCT job_title
FROM customers
WHERE job_industry_category IN ('IT', 'Financial Services')
AND job_title LIKE 'Senior%';

SELECT DISTINCT t.brand
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
WHERE c.job_industry_category = 'Financial Services';

SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
WHERE t.online_order = TRUE
AND t.brand IN ('Giant Bicycles', 'Norco Bicycles', 'Trek Bicycles')
LIMIT 10;

SELECT c.customer_id, c.first_name, c.last_name
FROM customers c
LEFT JOIN transaction t ON c.customer_id = t.customer_id
WHERE t.customer_id IS NULL;

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, MAX(t.standard_cost) AS max_standard_cost
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
WHERE c.job_industry_category = 'IT'
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY max_standard_cost DESC;

SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
WHERE c.job_industry_category IN ('IT', 'Health')
AND t.order_status = 'Approved'
AND t.transaction_date BETWEEN '2017-07-07' AND '2017-07-17';