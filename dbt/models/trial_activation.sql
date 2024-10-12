-- models/trial_activation.sql
SELECT
    organization_id,
    CASE WHEN (
            shift_created_goal >= 2 
            AND employee_invited_goal >= 1 
            AND punched_in_goal >= 1 
            AND entry_approved_goal >= 1 
            AND advanced_features_goal >= 2 
            ) 
            THEN true 
            ELSE false 
            END AS trial_activated
FROM {{ ref('trial_goals') }}
