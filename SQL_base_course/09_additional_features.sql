--9.4.1. 
SELECT t1.CompanyName, t2.CompanyName
FROM Customers t1, Customers t2
WHERE t1.CustomerID <> t2.CustomerID AND t1.Region IS NULL AND t2.Region IS NULL;

--9.4.2. 
SELECT t1.OrderID 
FROM Orders t1 
WHERE t1.CustomerID = ANY 
(SELECT CustomerID FROM Customers WHERE Region IS NULL);

--9.4.3. 
SELECT * 
FROM Orders t1 
WHERE t1.Freight > ANY 
(SELECT UnitPrice FROM Products);