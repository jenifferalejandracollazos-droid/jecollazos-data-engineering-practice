1.
SELECT nombre, saldo 
FROM clientes
WHERE saldo > (SELECT AVG(saldo) FROM clientes)
ORDER BY saldo DESC;

2.
SELECT cliente_id, COUNT(tipo)
FROM transacciones
GROUP BY cliente_id
ORDER BY COUNT(tipo) DESC;

3. 
SELECT clientes.nombre, SUM(transacciones.monto)
FROM clientes 
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
GROUP BY clientes.nombre
HAVING SUM(transacciones.monto) > 500000

4. 
SELECT clientes.id, transacciones.tipo
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
WHERE clientes.id NOT IN ('transacciones')

5.
SELECT clientes.nombre, clientes.ciudad, transacciones.monto
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id 
WHERE clientes.ciudad = 'Bogotá'
GROUP BY clientes.nombre