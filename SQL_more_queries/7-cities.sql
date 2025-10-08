-- 7-cities.sql
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    INDEX idx_state_id (state_id),
    CONSTRAINT cities_ibfk_1
        FOREIGN KEY (state_id) REFERENCES states(id)
);
