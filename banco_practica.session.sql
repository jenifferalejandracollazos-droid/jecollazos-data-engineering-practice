SELECT clientes.nombre, clientes.ciudad, COUNT(transacciones.tipo)
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
GROUP BY clientes.nombre
HAVING COUNT(transacciones.tipo) > 1
