-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 food_delivery.db
-- 2. Load this script: .read testing.sql
-- 3. Exit SQLite: .exit


-- You can use this to test your sql before you write it into your program.

-- Summaries --
select 
count(customer_id) as total_customers 
from customers;

select 
min(signup_date) as earliest_signup, 
max(signup_date) as latest_signup 
from customers;

select 
count(order_id) as total_orders, 
avg(order_total) as average_total, 
max(order_total) as highest_total, 
min(order_total) as lowest_total 
from orders;

select 
driver_id, hire_date 
from drivers
group by driver_id;