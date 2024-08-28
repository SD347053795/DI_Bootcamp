--Exercise 1
--Task 1: Rank Movies by Popularity within Each Genre
WITH RankedMovies AS (
    SELECT
        genre,
        title,
        popularity,
        RANK() OVER (
            PARTITION BY genre
            ORDER BY popularity DESC
        ) AS rank
    FROM movies
)
SELECT
    genre,
    title,
    rank
FROM RankedMovies
ORDER BY genre, rank;

--Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
WITH Quartiles AS (
    SELECT
        production_company,
        title,
        revenue,
        NTILE(4) OVER (
            PARTITION BY production_company
            ORDER BY revenue DESC
        ) AS quartile
    FROM movies
),
TopMovies AS (
    SELECT
        production_company,
        title,
        revenue,
        quartile
    FROM Quartiles
    WHERE quartile = 1 
    OR quartile = 2     
    OR quartile = 3     
)
SELECT
    production_company,
    title,
    revenue,
    quartile
FROM TopMovies
ORDER BY production_company, quartile, revenue DESC;

--Task 3: Calculate the Running Total of Movie Budgets for Each Genre
WITH RunningTotal AS (
    SELECT
        genre,
        title,
        budget,
        SUM(budget) OVER (
            PARTITION BY genre
            ORDER BY release_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS running_total_budget
    FROM movies
)
SELECT
    genre,
    title,
    budget,
    running_total_budget
FROM RunningTotal
ORDER BY genre, release_date;

--Task 4: Identify the Most Recent Movie for Each Genre
WITH MostRecentMovies AS (
    SELECT
        genre,
        title,
        release_date,
        -- Use FIRST_VALUE() to get the most recent movie based on release date within each genre
        FIRST_VALUE(title) OVER (
            PARTITION BY genre
            ORDER BY release_date DESC
        ) AS most_recent_title,
        FIRST_VALUE(release_date) OVER (
            PARTITION BY genre
            ORDER BY release_date DESC
        ) AS most_recent_release_date
    FROM movies
)
SELECT
    genre,
    most_recent_title AS title,
    most_recent_release_date AS release_date
FROM MostRecentMovies
GROUP BY genre, most_recent_title, most_recent_release_date
ORDER BY genre;


--Exercise 2
--Task 1: Rank Actors by Their Appearance in Movies
WITH ActorMovieCount AS (
    SELECT
        actor_name,
        COUNT(movie_id) AS movie_count
    FROM movies
    GROUP BY actor_name
),
RankedActors AS (
    SELECT
        actor_name,
        movie_count,
        DENSE_RANK() OVER (
            ORDER BY movie_count DESC
        ) AS rank
    FROM ActorMovieCount
)
SELECT
    actor_name,
    rank
FROM RankedActors
ORDER BY rank;

--Task 2: Identify the Top Director by Average Movie Rating
WITH AverageRatings AS (
    SELECT
        director_name,
        AVG(rating) AS average_rating
    FROM movies
    GROUP BY director_name
),
RankedDirectors AS (
    SELECT
        director_name,
        average_rating,
        RANK() OVER (
            ORDER BY average_rating DESC
        ) AS rank
    FROM AverageRatings
)
SELECT
    director_name,
    average_rating
FROM RankedDirectors
WHERE rank = 1
ORDER BY director_name;

--Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
WITH CumulativeRevenue AS (
    SELECT
        actor_name,
        movie_id,
        revenue,
        SUM(revenue) OVER (
            PARTITION BY actor_name
            ORDER BY movie_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS cumulative_revenue
    FROM movies
)
SELECT
    actor_name,
    cumulative_revenue
FROM CumulativeRevenue
GROUP BY actor_name, cumulative_revenue
ORDER BY actor_name;

--Task 4: Identify the Director Whose Movies Have the Highest Total Budget
WITH TotalBudgetPerDirector AS (
    SELECT
        director_name,
        SUM(budget) AS total_budget
    FROM movies
    GROUP BY director_name
),
RankedDirectors AS (
    SELECT
        director_name,
        total_budget,
        RANK() OVER (
            ORDER BY total_budget DESC
        ) AS rank
    FROM TotalBudgetPerDirector
)
SELECT
    director_name,
    total_budget
FROM RankedDirectors
WHERE rank = 1
ORDER BY director_name;
