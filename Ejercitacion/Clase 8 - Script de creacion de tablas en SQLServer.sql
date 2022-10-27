DROP TABLE Detalles;
DROP TABLE Facturas;
DROP TABLE Articulos;
DROP TABLE Clientes;


CREATE TABLE Clientes (
	ClienteID int NOT NULL IDENTITY(1,1),
	Nombre varchar(60) NOT NULL,
	Direccion varchar(80) NOT NULL,
	Ciudad varchar(30) NOT NULL,
	CP int NOT NULL,
	Pais varchar(30) NOT NULL,
	PRIMARY KEY (ClienteID)
); 

CREATE TABLE Articulos (
	ArticuloID int NOT NULL IDENTITY(1,1),
	Descripcion varchar(30) NOT NULL,
	Precio float NOT NULL,
	PRIMARY KEY (ArticuloID)
);

CREATE TABLE Facturas (
	FacturaID int NOT NULL IDENTITY(1,1),
	ClienteID int NOT NULL,
	Fecha date NOT NULL,
	PRIMARY KEY (FacturaID),
	FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)	
);

CREATE TABLE Detalles(
	FacturaID int NOT NULL,
	ArticuloID int NOT NULL,
	Cantidad int NOT NULL,
	Precio float NOT NULL,
	PRIMARY KEY (FacturaID, ArticuloID),
	FOREIGN KEY (FacturaID) REFERENCES Facturas(FacturaID),
	FOREIGN KEY (ArticuloID) REFERENCES Articulos(ArticuloID)
);


INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Resma A4', 148.0);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Resma Oficio', 150.0);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Resma Carta', 149.0);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Teclado', 1150.50);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Mouse', 848.0);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Lapicera azul BIC', 110.0);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Carpeta Oficio', 750.0);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Goma de borrar', 150.75);
INSERT INTO Articulos(Descripcion, Precio) 
VALUES ('Corrector líquido', 290);
INSERT INTO Articulos(Descripcion, Precio)
VALUES ('Repuesto agenda 2022', 780.75);
INSERT INTO Articulos(Descripcion, Precio)
VALUES ('Lapiz negro', 89);
INSERT INTO Articulos(Descripcion, Precio)
VALUES ('Sacapuntas', 97);


INSERT INTO Clientes(Nombre, Direccion, Ciudad, CP, Pais) 
VALUES ('Juan Lopez', 'Lima 956', 'CABA', 1582, 'Argentina');
INSERT INTO Clientes(Nombre, Direccion, Ciudad, CP, Pais) 
VALUES ('Esteban Fernandez', 'Perú 867', 'CABA', 2652, 'Argentina');
INSERT INTO Clientes(Nombre, Direccion, Ciudad, CP, Pais) 
VALUES ('Anibal Freijo', 'Estados Unidos 230', 'Lima', 4282, 'Perú');
INSERT INTO Clientes(Nombre, Direccion, Ciudad, CP, Pais) 
VALUES ('Anthony Kiedis', '152 street 4242', 'California', 122, 'Estados Unidos');
INSERT INTO Clientes(Nombre, Direccion, Ciudad, CP, Pais) 
VALUES ('Antonio Quispe', 'Lavalle 2552', 'La paz', 65182, 'Bolivia');
INSERT INTO Clientes(Nombre, Direccion, Ciudad, CP, Pais) 
VALUES ('Jorge Poroto', 'Av. Rivadavia 25425', 'Buenos Aires', 1522, 'Argentina');
INSERT INTO Clientes(Nombre, Direccion, Ciudad, CP, Pais) 
VALUES ('Manuel Benitez', 'De la palma 1254', 'Mburucuyá', 12822, 'Argentina');

DELETE FROM Clientes Where Nombre = 'Anthony Kiedis';


INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (1, '2022-10-05');
INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (1, '2021-10-06');
INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (3, '2022-02-16');
INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (3, '2021-12-26');
INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (3, '2021-10-06');
INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (2, '2021-08-12');
INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (7, '2022-01-28');
INSERT INTO Facturas (ClienteID, Fecha) 
VALUES (5, '2021-10-06');


/* Cliente 1*/
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (1, 1, 1, 148);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (1, 2, 1, 150);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (1, 3, 1, 149);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (2, 1, 2, 140);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (2, 2, 2, 140);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (2, 3, 2, 145);

/* Cliente 3*/
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (3, 4, 5, 1050.5);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (3, 5, 5, 840);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (4, 8, 10, 120);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (4, 9, 3, 250);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (4, 6, 11, 75);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (5, 7, 10, 500);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (5, 10, 1,  760.5);

/* Cliente 2*/ 
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (6, 10, 2,  760.5);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (6, 1, 12,  85.75);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (6, 3, 3,  90.75);

/* Cliente 7*/ 
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (7, 10, 3,  750.5);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (7, 1, 3,  145.5);

/* Cliente 5*/ 
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (8, 12, 10,  97);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (8, 11, 7,  85);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (8, 3, 4,  110);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (8, 1, 4,  120);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (8, 9, 2, 280);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (8, 6, 7, 105);
INSERT INTO Detalles (FacturaID, ArticuloID, Cantidad, Precio)
VALUES (8, 5, 1, 820.80);