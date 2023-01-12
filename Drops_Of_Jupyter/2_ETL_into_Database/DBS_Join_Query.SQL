select *
From individual 
INNER join general_health_status
on general_health_status."ID" = individual."ID"
where general_health_status."Diabetes" = 'yes';