select t1.table_name,t2.column_name,
t1.constraint_name,t1.constraint_type
from user_constraints t1 inner join 
user_cons_columns t2
on t1.constraint_name=t2.constraint_name
where lower(t1.table_name)=lower('&1');
