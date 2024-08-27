--Exercise 1
--Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.
CREATE TEMPORARY TABLE competitor_medal_counts (
  person_id INT,
  summer_medals INT,
  winter_medals INT
);
INSERT INTO competitor_medal_counts (person_id, summer_medals, winter_medals)
SELECT 
    pm_summer.person_id,
    pm_summer.summer_medals,
    pm_winter.winter_medals
FROM 
    (
        SELECT person_id, COUNT(medal_id) AS summer_medals
        FROM medals m
        JOIN games g ON m.games_id = g.id
        WHERE g.season = 'Summer'
        GROUP BY person_id
    ) AS pm_summer
JOIN 
    (
        SELECT person_id, COUNT(medal_id) AS winter_medals
        FROM medals m
        JOIN games g ON m.games_id = g.id
        WHERE g.season = 'Winter'
        GROUP BY person_id
    ) AS pm_winter
ON pm_summer.person_id = pm_winter.person_id;
SELECT * FROM competitor_medal_counts;


--Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.
CREATE TEMPORARY TABLE competitors_two_sports (
    person_id INT,
    total_medals INT
);
INSERT INTO competitors_two_sports (person_id, total_medals)
SELECT 
    person_id,
    COUNT(medal_id) AS total_medals
FROM 
    medals m
JOIN 
    events e ON m.event_id = e.id
GROUP BY 
    person_id
HAVING 
    COUNT(DISTINCT e.sport_id) = 2;
SELECT *
FROM competitors_two_sports
ORDER BY total_medals DESC
LIMIT 3;
SELECT * FROM competitors_two_sports;


--Exercise 2
--Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.
WITH max_medals_per_event AS (
    SELECT 
        gc.person_id,
        gc.games_id,
        MAX(gc.medals_won) AS max_medals
    FROM 
        games_competitor gc
    GROUP BY 
        gc.person_id, gc.games_id
),
total_medals_per_region AS (
    SELECT 
        nr.region_id,
        SUM(mmp.max_medals) AS total_medals
    FROM 
        max_medals_per_event mmp
    JOIN 
        person p ON mmp.person_id = p.id
    JOIN 
        person_region pr ON p.id = pr.person_id
    JOIN 
        noc_region nr ON pr.region_id = nr.id
    GROUP BY 
        nr.region_id
)
SELECT 
    nr.name AS region_name,
    tmr.total_medals
FROM 
    total_medals_per_region tmr
JOIN 
    noc_region nr ON tmr.region_id = nr.id
ORDER BY 
    tmr.total_medals DESC
LIMIT 5;


--Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.
CREATE TEMPORARY TABLE competitors_no_medals AS
SELECT 
    p.id AS person_id,
    p.first_name,
    p.last_name,
    COUNT(DISTINCT gc.games_id) AS games_participated
FROM 
    person p
JOIN 
    games_competitor gc ON p.id = gc.person_id
LEFT JOIN 
    medals m ON gc.person_id = m.person_id
WHERE 
    m.medal_id IS NULL 
GROUP BY 
    p.id, p.first_name, p.last_name
HAVING 
    COUNT(DISTINCT gc.games_id) > 3;
SELECT 
    person_id,
    first_name,
    last_name,
    games_participated
FROM 
    competitors_no_medals;
