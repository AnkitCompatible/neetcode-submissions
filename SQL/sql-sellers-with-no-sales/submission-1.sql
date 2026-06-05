Select seller_name from seller 
where seller_id not in (
select distinct on (seller_id) seller_id from orders where  sale_date<'2021-01-01' and sale_date>'2019-12-31'
)
order by seller_name

