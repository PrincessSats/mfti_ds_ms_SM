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
AND t.brand IN ('Giant Bicycles', 'Norco Bicycles', 'Trek Bicycles');

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

SELECT job_industry_category, COUNT(*) AS customer_count
FROM customers
GROUP BY job_industry_category
ORDER BY customer_count DESC;

SELECT 
    DATE_TRUNC('month', t.transaction_date) AS transaction_month,
    c.job_industry_category,
    SUM(t.list_price) AS total_sales
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY transaction_month, c.job_industry_category
ORDER BY transaction_month, c.job_industry_category;

SELECT t.brand, COUNT(*) AS online_order_count
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
WHERE c.job_industry_category = 'IT'
AND t.online_order = TRUE
AND t.order_status = 'Approved'
GROUP BY t.brand
ORDER BY online_order_count DESC;

SELECT c.customer_id, SUM(t.list_price) AS total_sales, 
       MAX(t.list_price) AS max_price, 
       MIN(t.list_price) AS min_price, 
       COUNT(t.transaction_id) AS transaction_count
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_sales DESC, transaction_count DESC;

SELECT DISTINCT c.customer_id, 
       SUM(t.list_price) OVER (PARTITION BY c.customer_id) AS total_sales,
       MAX(t.list_price) OVER (PARTITION BY c.customer_id) AS max_price,
       MIN(t.list_price) OVER (PARTITION BY c.customer_id) AS min_price,
       COUNT(t.transaction_id) OVER (PARTITION BY c.customer_id) AS transaction_count
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
ORDER BY total_sales DESC, transaction_count DESC;

SELECT c.first_name, c.last_name, SUM(t.list_price) AS total_sales
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_sales ASC;

SELECT c.first_name, c.last_name, SUM(t.list_price) AS total_sales
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_sales DESC;

SELECT DISTINCT ON (t.customer_id) t.customer_id, c.first_name, c.last_name, t.transaction_date, t.list_price
FROM transaction t
JOIN customers c ON t.customer_id = c.customer_id
ORDER BY t.customer_id, t.transaction_date ASC;

WITH transaction_intervals AS (
    SELECT t.customer_id, 
           c.first_name, c.last_name, c.job_title,
           LAG(t.transaction_date) OVER (PARTITION BY t.customer_id ORDER BY t.transaction_date) AS prev_transaction,
           t.transaction_date,
           t.transaction_date - LAG(t.transaction_date) OVER (PARTITION BY t.customer_id ORDER BY t.transaction_date) AS interval_days
    FROM transaction t
    JOIN customers c ON t.customer_id = c.customer_id
)
SELECT customer_id, first_name, last_name, job_title, interval_days
FROM transaction_intervals
WHERE interval_days IS NOT NULL
ORDER BY interval_days DESC;