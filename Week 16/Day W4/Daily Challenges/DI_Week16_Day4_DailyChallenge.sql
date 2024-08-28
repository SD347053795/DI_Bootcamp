--Task 1: Calculate the Average Budget Growth Rate for Each Production Company

WITH BudgetGrowth AS (
    SELECT
        production_company,
        movie_id,
        budget,
        LAG(budget) OVER (PARTITION BY production_company ORDER BY release_date) AS previous_budget,
        CASE
            WHEN LAG(budget) OVER (PARTITION BY production_company ORDER BY release_date) IS NULL THEN 0
            ELSE (budget - LAG(budget) OVER (PARTITION BY production_company ORDER BY release_date)) 
                 / LAG(budget) OVER (PARTITION BY production_company ORDER BY release_date) * 100
        END AS growth_rate
    FROM movies
),
AverageGrowth AS (
    SELECT
        production_company,
        AVG(growth_rate) AS average_growth_rate
    FROM BudgetGrowth
    GROUP BY production_company
)
SELECT * FROM AverageGrowth;

--Task 2: Determine the Most Consistently High-Rated Actor
WITH AverageRating AS (
    SELECT
        AVG(rating) AS avg_rating
    FROM movies
),
HighRatedMovies AS (
    SELECT
        movie_id,
        actor_id,
        rating
    FROM movies
    CROSS JOIN AverageRating
    WHERE rating > avg_rating
),
ActorMovieCount AS (
    SELECT
        actor_id,
        COUNT(movie_id) AS high_rated_movie_count
    FROM HighRatedMovies
    GROUP BY actor_id
),
MostConsistentActor AS (
    SELECT
        a.actor_name,
        amc.high_rated_movie_count
    FROM ActorMovieCount amc
    JOIN actors a ON amc.actor_id = a.actor_id
    ORDER BY amc.high_rated_movie_count DESC
    LIMIT 1
)
SELECT * FROM MostConsistentActor;

--Task 3: Calculate the Rolling Average Revenue for Each Genre
WITH RollingAverage AS (
    SELECT
        movie_id,
        genre,
        release_date,
        revenue,
        AVG(revenue) OVER (
            PARTITION BY genre
            ORDER BY release_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS rolling_avg_revenue
    FROM movies
)
SELECT * FROM RollingAverage;

--Task 4: Identify the Highest-Grossing Movie Series
WITH TotalRevenuePerSeries AS (
    SELECT
        series_id,
        SUM(revenue) AS total_revenue
    FROM movies
    GROUP BY series_id
),
HighestGrossingSeries AS (
    SELECT
        series_id,
        total_revenue,
        RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
    FROM TotalRevenuePerSeries
)
SELECT
    series_id,
    total_revenue
FROM HighestGrossingSeries
WHERE revenue_rank = 1;