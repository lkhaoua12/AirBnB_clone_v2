-- Creating database if not exists.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating a new user if not exists.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privleges on new user.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privleges to apply changes.
FLUSH PRIVILEGES;

