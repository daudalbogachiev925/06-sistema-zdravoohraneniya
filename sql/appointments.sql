SELECT v.id, v.visit_date,
       p.full_name AS patient,
       u.full_name AS doctor,
       d.spec
FROM visits v
JOIN patients p ON p.id = v.patient_id
JOIN doctors d ON d.id = v.doctor_id
JOIN users u ON u.id = d.user_id
WHERE v.visit_date::date = CURRENT_DATE
ORDER BY v.visit_date;
