SELECT v.id, v.visit_date, d.spec, u.full_name AS doctor,
       v.complaint, v.diagnosis_code, v.notes,
       (SELECT json_agg(json_build_object('drug', p.drug, 'dosage', p.dosage))
        FROM prescriptions p WHERE p.visit_id = v.id) AS prescriptions
FROM visits v
JOIN doctors d ON d.id = v.doctor_id
JOIN users u ON u.id = d.user_id
WHERE v.patient_id = $1
ORDER BY v.visit_date DESC;
