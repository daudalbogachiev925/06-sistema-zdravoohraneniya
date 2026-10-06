SELECT diagnosis_code,
       COUNT(*) AS cases,
       COUNT(DISTINCT patient_id) AS unique_patients,
       MIN(visit_date) AS first_case,
       MAX(visit_date) AS last_case
FROM visits
WHERE diagnosis_code IS NOT NULL
GROUP BY diagnosis_code
ORDER BY cases DESC
LIMIT 30;
