# Write your MySQL query statement below
select 
U.unique_id ,
e.name
from Employees e
left join EmployeeUNI U 
on e.id = U.id ;