from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ingest_raw_behavioral_events',
    default_args=default_args,
    description='Ingest Behavioral Events from s3 into Snowflake',
    schedule_interval='@once',  # Can be changed according to the needs
)

# Create Table
create_table_raw_behavioral_events_query = """
CREATE TABLE IF NOT EXIST raw_behavioral_events (
    organization_id VARCHAR(255),
    activity_name VARCHAR(255),
    activity_detail VARCHAR(255),
    timestamp TIMESTAMP
)
"""

create_table_task = SnowflakeOperator(
    task_id='create_table_raw_behavioral_events',
    snowflake_conn_id='sf_conn',  # You can define this in the Airflow connections.
    sql=create_table_raw_behavioral_events_query,
    dag=dag,
)

# Ingest csv from S3 Bucket into Snowflake
# I could have done this with the file in the Git repo but I think this way (the s3 bucket) is more realistic
# Also you can move the file the a different folder once its processed, so you avoid ingesting it multiple times

copy_into_query = """
COPY INTO raw_behavioral_events
FROM @behavioral_events/analytics_engineering_task.csv 
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = ',');
"""

load_data_task = SnowflakeOperator(
    task_id='load_csv_from_s3',
    snowflake_conn_id='sf_conn',  
    sql=copy_into_query,
    dag=dag,
)

create_table_task >> load_data_task
