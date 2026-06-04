-- Write your query below
select customer_id , customer_name
from customers c
where c.customer_id in (
    Select customer_id from orders where Product_name='A'
) AND c.customer_id in (
    Select customer_id from orders where Product_name='B'
) AND c.customer_id not in (
    Select customer_id from orders where Product_name='C'
) order by customer_name
