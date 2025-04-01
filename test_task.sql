SELECT
    DATE_TRUNC('week', leads.created_at) AS week_start,
    courses.type,
    COUNT(*) AS lead_count
FROM leads
JOIN courses ON leads.course_id = courses.id
GROUP BY week_start, courses.type
ORDER BY week_start DESC;


SELECT
    domains.country_name,
    COUNT(*) AS won_flex_lead_count
FROM leads
JOIN users ON leads.user_id = users.id
JOIN domains ON users.domain_id = domains.id
JOIN courses ON leads.course_id = courses.id
WHERE leads.status = 'WON'
    AND courses.type = 'FLEX'
    AND leads.created_at >= '2024-01-01'
GROUP BY domains.country_name;


SELECT
    users.email,
    leads.id AS lead_id,
    leads.lost_reason
FROM leads
JOIN users ON leads.user_id = users.id
JOIN courses ON leads.course_id = courses.id
WHERE leads.status = 'LOST'
    AND courses.type = 'FLEX'
    AND leads.created_at >= '2024-07-01';
