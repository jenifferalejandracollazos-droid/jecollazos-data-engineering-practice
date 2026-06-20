SELECT nombre, SELECT clientes.nombre, COUNT(transacciones.tipo)
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
GROUP BY clientes.nombre
HAVING COUNT(transacciones.tipo) > 1
ORDER BY COUNT(transacciones.tipo);