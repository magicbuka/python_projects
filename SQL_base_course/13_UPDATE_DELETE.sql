--13.3.1. 
UPDATE [Order Details]
SET Discount = 0.2
WHERE Quantity > 50;

--13.3.2.
UPDATE Contacts
SET City = 'Piter', Country = 'Russia'
WHERE City = 'Berlin' AND Country = 'Germany';

--13.3.3. 
INSERT INTO Shippers (CompanyName, Phone)
VALUES ('Speedy Express 2', '(503) 555-9831'),
       ('Federal Shipping', '(503) 555-9931');

DELETE FROM Shippers 
WHERE ShipperID > 3; 
