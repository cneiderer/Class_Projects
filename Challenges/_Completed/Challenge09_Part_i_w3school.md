# SQL Lab

_Structured Query Language_ (SQL) is a very useful [declarative language](http://en.wikipedia.org/wiki/Declarative_programming) for working with data. It is usually supported (with some variation) by relational databases. The tutorialspoint [SQL Quick Guide](http://www.tutorialspoint.com/sql/sql-quick-guide.htm) is a handy cheat sheet for a lot of the syntax. As a data user, access to data will usually consist of a more or less complicated `SELECT` statement.

For joining data with SQL, this [Visual Explanation of SQL Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) is quite good. One thing to note is that "join" will also often be known as "merge" in statistical software.

This lab uses the SQL playground provided in-browser by [W3Schools](http://www.w3schools.com/). Click [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) to go straight to the playground.

This is a pre-populated data environment with nothing to install and no risk of breaking anything. The data there is from a commonly-used example database ([info](http://northwinddatabase.codeplex.com/)). Nice!


## Guided

Let's walk through a few examples:

1) Retrieve all Customers from Madrid

```sql
SELECT
    * 
FROM
    Customers
WHERE
    City='Madrid';
```

2) How many customers are there in each city?

```sql
SELECT
    City, COUNT(*)
FROM
    Customers
GROUP BY
    City;
```

3) What is the most common city for customers? (And can you make it easy to find the correct answer?)

```sql
SELECT
    City, COUNT(*) AS count 
FROM
    Customers 
GROUP BY
    City 
ORDER BY
    count DESC;
```

4) What category has the most products?

```sql
SELECT
    CategoryName,
    COUNT(*) AS ProductCount
FROM
    Categories
  JOIN
    Products
  ON
    Categories.CategoryID = Products.CategoryID
GROUP BY
    CategoryName
ORDER BY 
    ProductCount DESC;
```


## Practice

 * Which customers are from the UK?
 ```sql
SELECT CustomerName 
FROM Customers
WHERE Country = 'UK'
 ```

 * What is the name of the customer who has the most orders?
 ```sql
SELECT Customers.CustomerName, COUNT(Orders.CustomerID) NumOrders
FROM Customers
JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerID
ORDER BY COUNT(Orders.CustomerID) DESC
 ```


 * Which supplier has the highest average product price?
 ```sql
SELECT Suppliers.SupplierName, AVG(Products.Price) AvgProdPrice
FROM Suppliers
JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID
ORDER BY AVG(Products.Price) DESC
 ```

 
 * How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
```sql
SELECT DISTINCT Customers.Country
FROM Customers
 ```

 
 * What category appears in the most orders?
 ```sql
SELECT Categories.CategoryName, OrderDetails.Quantity
FROM OrderDetails
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
JOIN Categories
ON Products.CategoryID = Categories.CategoryID
GROUP BY Products.CategoryID
ORDER BY OrderDetails.Quantity DESC
 ```

 
 * What was the total cost for each order?
 ```sql
SELECT OrderDetails.OrderID, SUM(OrderDetails.Quantity * Products.Price) Cost
FROM OrderDetails
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
GROUP BY OrderDetails.OrderID
 ```

 * Which employee made the most sales (by total cost)?
 ```sql
SELECT Orders.EmployeeID, Employees.LastName, Employees.FirstName, SUM(OrderDetails.Quantity * Products.Price) Sales
FROM OrderDetails
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
JOIN Orders
ON OrderDetails.OrderID = Orders.OrderID
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY Sales DESC
 ```

 * Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
 ```sql
SELECT * 
FROM Employees
WHERE Employees.Notes LIKE '%BS%'
 ```

 * Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
```sql
SELECT Products.SupplierID, Suppliers.SupplierName, COUNT(Products.ProductID), AVG(Products.Price)
FROM Products
JOIN Suppliers
ON Products.SupplierID = Suppliers.SupplierID
GROUP BY Products.SupplierID
HAVING COUNT(Products.ProductID) > 2
 ```

 