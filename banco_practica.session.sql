SELECT nombre, ciudad, saldo
FROM clientes
WHERE ciudad IN ('Cali', 'Bogotá')
ORDER BY nombre ASC;