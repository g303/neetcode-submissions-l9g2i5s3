CREATE TABLE olympic_medals (
    country TEXT,
    year INTEGER,
    total_medals INTEGER
);

INSERT INTO olympic_medals (country, year, total_medals) VALUES
    ('USA', 2021, 22),
    ('China', 2021, 38),
    ('UK', 2021, 77),
    ('Russia', 2021, 20),
    ('USA', 2022, 20),
    ('China', 2022, 68),
    ('UK', 2022, 24),
    ('Russia', 2022, 16),
    ('USA', 2023, 29),
    ('China', 2023, 49),
    ('UK', 2023, 20),
    ('Russia', 2023, 14);
-- Do not modify above this line. --

select country from (
SELECT country, sum(total_medals) as sum_total
FROM olympic_medals 
group by country) as t1  
where sum_total > 100
--where sum(total_medals)  > 100
--GROUP BY country HAVING SUM(total_medals)>100
order by country desc;




