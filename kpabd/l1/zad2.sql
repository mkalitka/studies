SELECT pm.Name, COUNT(*) cnt
FROM SalesLT.Product p
  LEFT JOIN SalesLT.ProductModel pm ON p.ProductModelID = pm.ProductModelID
GROUP BY pm.ProductModelID, pm.Name
HAVING cnt > 1
