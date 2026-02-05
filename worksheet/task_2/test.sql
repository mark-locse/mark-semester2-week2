SELECT c.customer_name as "Customer Name", sum(t.price) as "Total Spent"
FROM customers c
JOIN tickets t ON c.customer_id=t.customer_id
GROUP BY c.customer_id, c.customer_name 
HAVING count(t.ticket_id)>=1
ORDER BY sum(t.price) desc
LIMIT 5;