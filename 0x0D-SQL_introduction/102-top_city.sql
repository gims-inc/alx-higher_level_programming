-- Dispaly the top 3 of cities temprature during july and august
select city, avg(value) as avg_temp from temperatures where month = 8 or month = 7  group by city order by avg_temp desc limit 3;
