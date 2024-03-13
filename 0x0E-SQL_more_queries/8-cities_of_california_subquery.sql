-- lists all the cities of California that can be found in
-- the database hbtn_0d_usa.
SELECT * FROM cities
WHERE EXISTS (
    SELECT 1 FROM states WHERE states.id = cities.state_id AND states.name = 'California'
)
ORDER BY id;