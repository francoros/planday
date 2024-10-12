# PLANDAY

I could have done it just ingesting the file in a table, and then just run some SQL queries, but I've chosen to did it like this because I think is closer to the real situation.

# The pipeline was built using Apache Airflow for orchestration and DBT for SQL-based transformations, connected to a Snowflake data warehouse. The folder structure is not exactly as its going to be (I don't have airdflow and dbt installed), its like this just for understanding

## Implemented Metrics

Activation Rate: The percentage of organizations that achieve trial activation by completing all defined goals (e.g., creating shifts, inviting employees, etc.).
Goal Completion Rates: Percentage of organizations completing each individual goal (Shift Created, Employee Invited, Punch In, etc.)
Average Time to Activation: This metric calculates the time it takes for organizations to complete all goals and achieve trial activation.

## Project Structure

The project consists of two main parts:

# 1. Airflow Pipeline
The Airflow DAG orchestrates the following steps:

Ingestion: Ingest raw event data into the raw_behavioral_events table in Snowflake.

dbt Transformation: Trigger dbt models to perform data transformations, creating two key models:

trial_goals: Tracks whether each organization has completed specific trial goals.
trial_activation: Tracks whether an organization has completed all the goals, marking them as "trial activated."

Quality Checks: After the dbt transformation, I created some minor queries to run in Snowflake and check the quality of the information

# 2. dbt Models
The dbt project follows a layered approach:

Staging Layer: Raw data is loaded into the raw_behavioral_events table without any transformations.
Transformation Layer: Business logic is applied to aggregate trial goals (e.g., counting shifts created, employees invited) and produce the trial_goals table.
Data Marts Layer: The final trial_activation table is created, showing which organizations have fully completed all trial goals.

# 3. Visualisation

Last, some charts or dashboards can be created out of it with the desired tool, i.e: PowerBi, Tableau, Looker, etc

