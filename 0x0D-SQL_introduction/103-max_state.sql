-- Display max tempratures of each state ordered by state name
select state, max(value) as max_temp from temperatures group by state order by state asc;
