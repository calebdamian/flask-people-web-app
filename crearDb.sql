CREATE DATABASE pytestcdna;
USE pytestcdna;
DROP TABLE IF EXISTS Persona;
CREATE TABLE Persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    edad INT,
    direccion VARCHAR(255),
    correo VARCHAR(255)
);