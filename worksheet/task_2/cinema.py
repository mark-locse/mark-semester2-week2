"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3

conn = sqlite3.connect("tickets.db")
def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    query = '''SELECT f.title AS "Film Title", s.screen AS Screen, t.price AS Price
FROM films f, screenings s, tickets t, customers c
WHERE f.film_id=s.film_id AND s.screening_id=t.screening_id
AND c.customer_id=t.customer_id AND c.customer_id=?
ORDER BY f.title;'''
    result = conn.execute(query, (customer_id,))
    return result.fetchall()

def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    query = '''SELECT s.screening_id AS "Screening ID", f.title AS "Film Title", count(t.ticket_id) AS "Tickets Sold"
    FROM screenings s JOIN films f ON f.film_id=s.film_id 
    LEFT JOIN tickets t ON s.screening_id=t.screening_id
    GROUP BY s.screening_id, f.title
    ORDER BY count(t.ticket_id) desc;'''
    result = conn.execute(query)
    return result.fetchall()


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    query = '''SELECT c.customer_name as "Customer Name", sum(t.price) as "Total Spent"
FROM customers c
JOIN tickets t ON c.customer_id=t.customer_id
GROUP BY c.customer_id, c.customer_name 
HAVING count(t.ticket_id)>=1
ORDER BY sum(t.price) desc
LIMIT ?;'''
    result = conn.execute(query, (limit,))
    return result.fetchall()