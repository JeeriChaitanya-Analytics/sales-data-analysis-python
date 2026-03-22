select employee_id, department_id, department_name, row_number() over (order by salary desc) as rn
from employee_table as e
join department_table as d
on e.department_id = d.department_id
where rn = 1;


select employee_id, employee_name, datediff(Year,joining_date, current_date()) as Total_experience_in_years
from employee_table;

							
	EMP_id	Status						
	1	A						
	2	A						
	3	I						
	4	I						
	5	A	

select emp_id, 
case when status = 'A' then 'I 
when status = 'I then 'A'
end as status
from employee_table;



A			B				
	col1			col1				
	1			1				
	1			1				
	2			2				
	3 

1   1
1   1
1   1
1   1
2   2 


select employee_name, count(*) as Total_count
from employee_table
group by employee_name
having count(*) > 1;





