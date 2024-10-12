-- ROW COUNT
SELECT COUNT(*) FROM raw_behavioral_events AS raw_count; 
SELECT COUNT(*) FROM trial_goals AS goals_count; --This should be the same as the unique organization_id in the prev query

-- Check for NULL values in organization_id and goal columns
SELECT COUNT(*) FROM trial_goals WHERE organization_id IS NULL;

SELECT COUNT(*) FROM trial_goals WHERE shift_created IS NULL OR employee_invited IS NULL OR punched_in IS NULL OR punch_in_approved IS NULL OR advanced_features_viewed IS NULL;

-- Check for duplicate organization_id values
SELECT organization_id, COUNT(*) 
FROM trial_goals
GROUP BY organization_id
HAVING COUNT(*) > 1;

-- Check if any organizations in raw_behavioral_events are missing in trial_goals
SELECT organization_id 
FROM trial_activation
WHERE organization_id NOT IN (SELECT organization_id FROM trial_goals);

-- Check if an organization with exactly 2 shifts is considered successful for that goal
SELECT organization_id, COUNT(*) AS shift_count
FROM raw_trial_activities
WHERE activity_name = 'Shift.Created'
GROUP BY organization_id
HAVING shift_count = 2;

-- Check the result in trial_goals for the corresponding organizations
SELECT * FROM trial_goals WHERE organization_id IN (
    SELECT organization_id
    FROM raw_trial_activities
    WHERE activity_name = 'Shift.Created'
    GROUP BY organization_id
    HAVING COUNT(*) = 2
);


