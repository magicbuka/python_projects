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
/**��������� ������� ���������� �� ���� �������, ������� �� ������� ��� ������� ������
� ������ ������ � ������� Orders ��� CustomerID ������� �������� PARIS � FISSA, 
� � ������� Customers ����� CustomerID ������� � ��� ��� ������� �������� ���� CompanyName
����� ������� � ��������� ���������� ��� �������**/

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