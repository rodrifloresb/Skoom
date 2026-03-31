-- ======================
-- SCHOOLS
-- ======================
INSERT IGNORE INTO schools (name, mail, password, phoneNumber, address, logo) VALUES
('Colegio San Martin', 'sanmartin@mail.com', '1234', '3511111111', 'Av. Siempre Viva 123', NULL),
('Colegio Belgrano', 'belgrano@mail.com', '1234', '3512222222', 'Calle Falsa 456', NULL),
('Colegio Nacional', 'nacional@mail.com', '1234', '3513333333', 'Boulevard Central 789', NULL),
('Colegio Tecnico', 'tecnico@mail.com', '1234', '3514444444', 'Av. Industrial 101', NULL),
('Colegio Privado Sur', 'sur@mail.com', '1234', '3515555555', 'Ruta 20 km 5', NULL);

-- ======================
-- TUTORS
-- ======================
INSERT IGNORE INTO tutors (firstName, lastName, mail, password, phoneNumber, address, logo) VALUES
('Carlos', 'Gomez', 'carlos@mail.com', '1234', '3516000001', 'Barrio Centro 123', NULL),
('Maria', 'Lopez', 'maria@mail.com', '1234', '3516000002', 'Barrio Norte 456', NULL),
('Juan', 'Perez', 'juan@mail.com', '1234', '3516000003', 'Barrio Sur 789', NULL),
('Ana', 'Martinez', 'ana@mail.com', '1234', '3516000004', 'Barrio Este 321', NULL),
('Luis', 'Fernandez', 'luis@mail.com', '1234', '3516000005', 'Barrio Oeste 654', NULL);

-- ======================
-- STUDENTS
-- ======================
INSERT IGNORE INTO students (firstName, lastName, tuition, course, tutor_id, school_id) VALUES
-- Colegio 1
('Pedro', 'Gomez', 100, '1A', 1, 1),
('Lucia', 'Gomez', 101, '2B', 1, 1),

-- Colegio 2
('Sofia', 'Lopez', 100, '1A', 2, 2),
('Martin', 'Lopez', 102, '3C', 2, 2),

-- Colegio 3
('Diego', 'Perez', 103, '2A', 3, 3),
('Valentina', 'Perez', 104, '4B', 3, 3),

-- Colegio 4
('Camila', 'Martinez', 105, '1C', 4, 4),

-- Colegio 5
('Mateo', 'Fernandez', 100, '2A', 5, 5);