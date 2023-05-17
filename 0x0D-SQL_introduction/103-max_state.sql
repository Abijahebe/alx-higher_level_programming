-- Displays the max temperature of each state
-- (ordered by State name).

SELECT stste, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY stste ASC;
