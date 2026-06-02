-- Write your query below
Select name 
from customers 
where id NOT IN ( Select customer_id from orders);