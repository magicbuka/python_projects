--10.4.1. 
SELECT
Products.ProductName, [Order Details].UnitPrice
FROM
Products
JOIN [Order Details]
WHERE
Products.ProductID = [Order Details].ProductID 
AND [Order Details].UnitPrice < 20;

--10.4.2. 
SELECT Orders.Freight, 
Customers.CompanyName
FROM Orders 
FULL JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
ORDER BY Freight;
/**Результат запроса увеличился за счет записей, которые не подошли под условие отбора (поэтому поля заполняются значением NULL).
В данном случае в таблице Orders нет CustomerID имеющих значения PARIS и FISSA, 
а в таблице Customers такие CustomerID имеются и для них имеются значения поля CompanyName
Иными словами у некоторых заказчиков нет заказов**/

--10.4.3. 
SELECT Products.ProductName, 
[Order Details].UnitPrice
FROM Products 
CROSS JOIN [Order Details]
WHERE Products.ProductID = [Order Details].ProductID;

--10.4.4. 
SELECT Products.ProductName, 
[Order Details].UnitPrice
FROM Products 
JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID
