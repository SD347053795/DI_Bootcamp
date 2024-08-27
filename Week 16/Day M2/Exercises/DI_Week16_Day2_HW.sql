--Exercise 1
--Task 1: Average Age of Competitors by Medal Type
SELECT
    medal_type,
    AVG(age) AS avg_age
FROM
    competitors
WHERE
    competitor_id IN (
        SELECT DISTINCT competitor_id
        FROM medals
        WHERE medal_count > 0
    )
GROUP BY
    medal_type;


--Task 2: Top 5 Regions with Most Unique Competitors in Multiple Events
SELECT
    region,
    COUNT(DISTINCT competitor_id) AS unique_competitors_count
FROM (
    SELECT
        competitor_id,
        region,
        COUNT(DISTINCT event) AS events_count
    FROM
        competitors_events
    GROUP BY
        competitor_id, region
    HAVING
        COUNT(DISTINCT event) > 3
) AS subquery
GROUP BY
    region
ORDER BY
    unique_competitors_count DESC
LIMIT 5;


--Task 3: Temporary Table for Total Medals Won
CREATE TEMPORARY TABLE temp_total_medals AS
SELECT
    competitor_id,
    COUNT(*) AS total_medals
FROM
    medals
GROUP BY
    competitor_id;

SELECT *
FROM temp_total_medals
WHERE total_medals > 2;


--Task 4: Delete Competitors with No Medals from Temporary Table
DELETE FROM temp_total_medals
WHERE competitor_id NOT IN (
    SELECT competitor_id
    FROM medals
);


--Exercise 2
--Task 1: Update the heights of competitors based on the average height of competitors from the same region
UPDATE person
SET height = (
  SELECT AVG(p2.height)
  FROM person p2
  JOIN person_region pr ON p2.id = pr.person_id
  WHERE pr.region_id = (
    SELECT region_id
    FROM person_region
    WHERE person_id = person.id
  )
)
WHERE height IS NULL; 


--Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated
--Part 1
CREATE TEMPORARY TABLE multi_event_competitors (
  person_id INT,
  games_id INT,
  total_events INT
);

--Part 2
INSERT INTO multi_event_competitors (person_id, games_id, total_events)
SELECT person_id, games_id, COUNT(*)
FROM event_participation
GROUP BY person_id, games_id
HAVING COUNT(*) > 1;


--Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average
WITH overall_avg AS (
  SELECT AVG(medal_count) AS avg_medals
  FROM (
    SELECT person_id, COUNT(medal_id) AS medal_count
    FROM medals
    GROUP BY person_id
  ) AS subquery
)
SELECT region_id
FROM person_region pr
JOIN (
  SELECT person_id, COUNT(medal_id) AS medal_count
  FROM medals
  GROUP BY person_id
) AS person_medals ON pr.person_id = person_medals.person_id
GROUP BY region_id
HAVING AVG(person_medals.medal_count) > (SELECT avg_medals FROM overall_avg);


--Task 4: Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games
--Step 1
CREATE TEMPORARY TABLE season_participation (
  person_id INT,
  has_summer_participated BOOLEAN,
  has_winter_participated BOOLEAN
);

--Step 2
INSERT INTO season_participation (person_id, has_summer_participated, has_winter_participated)
SELECT person_id,
  MAX(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS has_summer_participated,
  MAX(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS has_winter_participated
FROM games_competitor gc
JOIN games g ON gc.games_id = g.id
GROUP BY person_id;

--Step 3
SELECT person_id
FROM season_participation
WHERE has_summer_participated = 1 AND has_winter_participated = 1;

