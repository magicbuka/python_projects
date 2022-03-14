--12.3.1.
INSERT INTO Employees
           (LastName,
           FirstName,
           Title,
           TitleOfCourtesy,
           BirthDate,
           HireDate,
           Address,
           City,
           PostalCode,
           Country,
           HomePhone,
           ReportsTo)
     VALUES
           ('Fry',
           'Harry',
           'Sales Representative',
           'Mr.',
           '1957-08-24 00:00:00.000',
           '1993-10-17 00:00:00.000',
           'Coventry House Miner Rd.',
           'London',
           'SW1 8JR',
           'UK',
           '(71) 555-4850',
           5)

--12.3.2. 
INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID)
VALUES (11, 14450),
       (11, 11747)

--12.3.3. 
INSERT INTO Orders
           (CustomerID,
           EmployeeID,
           OrderDate,
           RequiredDate,
           ShippedDate,
           ShipVia,
           Freight,
           ShipName,
           ShipAddress,
           ShipCity,
           ShipPostalCode,
           ShipCountry)
     VALUES
           ('TOMSP',
           11,
           '1997-02-14 00:00:00.000',
           '1997-03-14 00:00:00.000',
           '1997-03-07 00:00:00.000',
           2,
           '14,6800',
           'Toms Spezialitäten',
           'Luisenstr. 48',
           'Münster',
           '44087',
           'Germany')

--Конфликтов не возниикло. 
