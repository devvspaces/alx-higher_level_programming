-- List all databases in the server
CREATE TABLE IF NOT EXISTS second_table(
id INT,
name VARCHAR(256),
score INT
);
BEGIN work
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8)
COMMIT work;

select score, name from second_table order by score;

update second_table set score=10 where name = 'Bob';

delete second_table where score <= 5;

select score from second_table group by count(name);

select score, name from second_table where is not null name;