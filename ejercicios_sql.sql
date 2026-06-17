-- Clientes ordenados de mayor a menor saldo
SELECT nombre, saldo
FROM clientes
ORDER BY saldo DESC;

-- Ciudades con más de 1 cliente
SELECT ciudad, COUNT(*)
FROM clientes
GROUP BY ciudad
HAVING COUNT(*) > 1;

-- Nombre del cliente y total de sus transacciones
SELECT clientes.nombre, SUM(transacciones.monto)
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
GROUP BY clientes.nombre;

-- Clientes con saldo mayor al promedio
SELECT nombre, ciudad, saldo
FROM clientes
WHERE saldo > (SELECT AVG(saldo) FROM clientes);

-- Nombre del cliente y total de transacciones, solo los que superen 600.000
SELECT clientes.nombre, SUM(transacciones.monto)
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
GROUP BY clientes.nombre
HAVING SUM(transacciones.monto) > 600000
ORDER BY SUM(transacciones.monto) DESC;

-- Transacciones de clientes de Cali
SELECT clientes.nombre, transacciones.monto
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
WHERE clientes.ciudad = 'Cali'
ORDER BY transacciones.monto DESC;

-- Transacciones con monto mayor al promedio
SELECT clientes.nombre, transacciones.monto
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
WHERE transacciones.monto > (SELECT AVG(monto) FROM transacciones);

-- Clientes sin transacciones
SELECT nombre, ciudad
FROM clientes
WHERE id NOT IN (SELECT cliente_id FROM transacciones);

-- Nombre, saldo y número de transacciones por cliente
SELECT clientes.nombre, clientes.saldo, COUNT(*)
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
GROUP BY clientes.nombre
ORDER BY COUNT(*) DESC;

-- Promedio de monto por tipo de transacción
SELECT tipo, AVG(monto)
FROM transacciones
GROUP BY tipo
ORDER BY AVG(monto) DESC;

-- Clientes con más de 1 transacción
SELECT clientes.nombre, clientes.saldo, COUNT(*)
FROM clientes
INNER JOIN transacciones ON clientes.id = transacciones.cliente_id
GROUP BY clientes.nombre
HAVING COUNT(*) > 1;

-- Clientes de Bogotá o Cali ordenados alfabéticamente
SELECT nombre, ciudad, saldo
FROM clientes
WHERE ciudad IN ('Cali', 'Bogotá')
ORDER BY nombre ASC;