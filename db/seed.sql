INSERT INTO users (login, password_hash, role, full_name) VALUES
('admin','hash','admin','Администратор'),
('doc1','hash','doctor','Иванов И.И.'),
('doc2','hash','doctor','Петрова П.П.'),
('reg1','hash','registrar','Смирнова С.С.');

INSERT INTO doctors (user_id, spec, cabinet) VALUES
(2,'Терапевт','101'),(3,'Кардиолог','205');

INSERT INTO patients (full_name, birth, gender, policy, phone) VALUES
('Сидоров А.А.','1985-05-05','M','POL001','+7900'),
('Кузнецова М.И.','1990-08-15','F','POL002','+7901'),
('Орлов В.П.','1978-02-20','M','POL003','+7902');

INSERT INTO visits (patient_id, doctor_id, visit_date, complaint, diagnosis_code) VALUES
(1,1,'2024-01-10 10:00','Кашель','J06.9'),
(1,2,'2024-01-20 14:00','Давление','I10'),
(2,1,'2024-01-12 09:30','Головная боль','G43'),
(3,2,'2024-02-01 11:00','Боль в груди','I20');

INSERT INTO prescriptions (visit_id, drug, dosage, duration_days) VALUES
(1,'Амброксол','30мг 3р/д',7),
(2,'Эналаприл','10мг 1р/д',30),
(3,'Ибупрофен','400мг',3);

INSERT INTO lab_results (patient_id, test_name, result, unit, normal_range) VALUES
(1,'Гемоглобин','135','г/л','120-160'),
(1,'Лейкоциты','7.5','10^9/л','4-9'),
(2,'Холестерин','6.2','ммоль/л','<5.2');
