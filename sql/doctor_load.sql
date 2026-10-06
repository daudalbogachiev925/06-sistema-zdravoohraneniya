SELECT u.full_name AS doctor, d.spec,
       COUNT(v.id) AS total_visits,
       COUNT(v.id) FILTER (WHERE v.visit_date >= NOW() - INTERVAL '30 days') AS last_30d,
       COUNT(v.id) FILTER (WHERE v.visit_date >= NOW() - INTERVAL '7 days') AS last_7d
FROM doctors d
JOIN users u ON u.id = d.user_id
LEFT JOIN visits v ON v.doctor_id = d.id
GROUP BY u.full_name, d.spec
ORDER BY total_visits DESC;
