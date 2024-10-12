-- models/trial_goals.sql
WITH raw_data AS (
    SELECT
        organization_id,
        activity_name,
        activity_detail
    FROM {{ ref('raw_behavioral_events') }}
)

SELECT
    organization_id,
    COUNT(CASE WHEN activity_name = 'Shift.Created' THEN 1 END) AS shift_created,
    COUNT(CASE WHEN activity_name = 'Hr.Employee.Invited' THEN 1 END) AS employee_invited,
    COUNT(CASE WHEN activity_name = 'PunchClock.PunchedIn' THEN 1 END) AS punched_in,
    COUNT(CASE WHEN activity_name = 'PunchClock.Approvals.EntryApproved' THEN 1 END) AS punch_in_approved,
    COUNT(CASE WHEN activity_name = 'Page.Viewed' AND activity_detail IN ('revenue', 'integrations-overview', 'absence-accounts', 'availability') THEN 1 END) AS advanced_features_viewed
FROM raw_data
GROUP BY organization_id
