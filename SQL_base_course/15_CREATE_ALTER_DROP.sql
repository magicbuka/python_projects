--15.7.
CREATE DATABASE MyTest;

USE MyTest;

CREATE TABLE 
	Region ( 
    RegionID int PRIMARY KEY, 
	RegionDescription nchar(50) NOT NULL ); 

ALTER TABLE Region ADD Help nchar(16); 

CREATE TABLE 
	Territories(
	TerritoryID nvarchar(20) NOT NULL PRIMARY KEY,
	TerritoryDescription nchar(50) NOT NULL,
	RegionID int FOREIGN KEY(RegionID) REFERENCES Region (RegionID)); 

INSERT INTO Region (RegionID, RegionDescription)
VALUES (1, 'Eastern'),
       (2, 'Western')

INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID)
VALUES (01581, 'Westboro', 1),
       (01730, 'Bedford', 2)

