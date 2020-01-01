CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  origin VARCHAR NOT NULL,
  destination VARCHAR NOT NULL,
  duration INTEGER NOT NULL
);

CREATE TABLE passengers(
  flight_id INTEGER NOT NULL,
  name VARCHAR NOT NULL  
);
