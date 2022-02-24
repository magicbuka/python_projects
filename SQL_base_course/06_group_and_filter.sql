--6.3.1. 
SELECT ContactType,
COUNT(ContactType) AS Contacts_count
FROM Contacts
WHERE ContactType IS NOT NULL
GROUP BY ContactType

--6.3.2. 
SELECT 
CategoryId, 
AVG(UnitPrice) AS Average_UnitPrice
FROM Products
GROUP BY CategoryId
ORDER BY Average_UnitPrice