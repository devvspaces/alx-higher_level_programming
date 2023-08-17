-- Lists all records of the table second_table that have a name that is not NULL,
-- sorted by score in descending order.
SELECT
    score,
    name
FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
