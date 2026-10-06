CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    login TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('admin','doctor','nurse','registrar')),
    full_name TEXT,
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE patients (
    id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth DATE NOT NULL,
    gender TEXT CHECK (gender IN ('M','F')),
    policy TEXT UNIQUE NOT NULL,
    phone TEXT,
    address TEXT,
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE doctors (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(id),
    spec TEXT NOT NULL,
    cabinet TEXT,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE visits (
    id BIGSERIAL PRIMARY KEY,
    patient_id BIGINT REFERENCES patients(id),
    doctor_id BIGINT REFERENCES doctors(id),
    visit_date TIMESTAMP NOT NULL,
    complaint TEXT,
    diagnosis_code TEXT,
    notes TEXT,
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE prescriptions (
    id BIGSERIAL PRIMARY KEY,
    visit_id BIGINT REFERENCES visits(id) ON DELETE CASCADE,
    drug TEXT NOT NULL,
    dosage TEXT,
    duration_days INT,
    notes TEXT
);

CREATE TABLE lab_results (
    id BIGSERIAL PRIMARY KEY,
    patient_id BIGINT REFERENCES patients(id),
    test_name TEXT NOT NULL,
    result TEXT,
    unit TEXT,
    normal_range TEXT,
    taken_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE audit_log (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT,
    action TEXT NOT NULL,
    entity TEXT NOT NULL,
    entity_id BIGINT,
    ts TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_visits_patient ON visits(patient_id);
CREATE INDEX idx_visits_doctor ON visits(doctor_id);
CREATE INDEX idx_visits_date ON visits(visit_date);
CREATE INDEX idx_lab_patient ON lab_results(patient_id);
