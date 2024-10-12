import pandas as pd
import snowflake.connector

def connect_to_snowflake(user, password, account, warehouse, database, schema):
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )
    return conn

def load_data(conn, query):
    return pd.read_sql(query, conn)

# Function to calculate the activation rate
def calculate_activation_rate(trial_activation_df):
    activation_rate = trial_activation_df['trial_activated'].mean() * 100
    return activation_rate

# Function to calculate goal completion rates
def calculate_goal_completion_rates(trial_goals_df):
    goal_completion_rates = {
        'Shift Created': trial_goals_df['shift_created'].mean() * 100,
        'Employee Invited': trial_goals_df['employee_invited'].mean() * 100,
        'Punched In': trial_goals_df['punched_in'].mean() * 100,
        'Punch In Approved': trial_goals_df['punch_in_approved'].mean() * 100,
        'Advanced Features Viewed': trial_goals_df['advanced_features_viewed'].mean() * 100
    }
    return goal_completion_rates


# Could be a function to calculate the time to activation, but its needed the timestamp when it passes all the requirements to get activated

def run_analyses(user, password, account, warehouse, database, schema):
    
    # Connect to Snowflake
    conn = connect_to_snowflake(user, password, account, warehouse, database, schema)
    
    trial_goals_query = "SELECT * FROM trial_goals"
    trial_activation_query = "SELECT * FROM trial_activation"

    # Load data from Snowflake
    trial_goals_df = load_data(conn, trial_goals_query)
    trial_activation_df = load_data(conn, trial_activation_query)
    
    activation_rate = calculate_activation_rate(trial_activation_df)
    goal_completion_rates = calculate_goal_completion_rates(trial_goals_df)
    
    # Print Results
    print(f"Activation Rate: {activation_rate:.2f}%")
    for goal, rate in goal_completion_rates.items():
        print(f"{goal} Completion Rate: {rate:.2f}%")
    
    conn.close()

if __name__ == "__main__":
    run_analyses(
        user='USERNAME',
        password='PASSWORD',
        account='ACCOUNT',
        warehouse='WAREHOUSE',
        database='DATABASE',
        schema='SCHEMA'
    )
