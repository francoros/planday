# **PLANDAY 

I could have simply ingested the file into a table and run SQL queries to generate the results. However, I chose to build it this way because I believe it more closely simulates a real-world data pipeline scenario.

---

## **Pipeline Overview**

The pipeline was built using **Apache Airflow** for orchestration and **dbt** (Data Build Tool) for SQL-based transformations, connected to a **Snowflake** data warehouse. The folder structure presented here is a simplified version for demonstration purposes, as I don't have Airflow and dbt installed locally. It is structured this way to illustrate the flow and logic behind the implementation.

---

## **Implemented Metrics**

1. **Activation Rate**:  
   The percentage of organizations that achieve trial activation by completing all defined goals (e.g., creating shifts, inviting employees, etc.).

2. **Goal Completion Rates**:  
   The percentage of organizations completing each individual goal (Shift Created, Employee Invited, Punch In, etc.).

3. **Average Time to Activation**:  
   The time it takes for organizations to complete all goals and achieve trial activation.
   (This is not done because the timestamp when the organization reaches the goal is not setted, but it can assumed)

---

## **Project Structure**

### **1. Airflow Pipeline**

The **Airflow DAG** orchestrates the following steps:

- **Ingestion**:  
  Ingest raw event data into the `raw_behavioral_events` table in Snowflake.
  
- **dbt Transformation**:  
  Trigger **dbt** models to perform data transformations, creating two key models:
  - **`trial_goals`**: Tracks whether each organization has completed specific trial goals.
  - **`trial_activation`**: Tracks whether an organization has completed all goals and is marked as "trial activated."

- **Quality Checks**:  
  After the dbt transformations, I created a few minor queries in Snowflake to check the quality and consistency of the transformed data.

---

### **2. dbt Models**

The **dbt project** follows a structured, layered approach:

- **Staging Layer**:  
  Raw data is loaded into the `raw_behavioral_events` table without any transformations.

- **Transformation Layer**:  
  Business logic is applied to aggregate trial goals (e.g., counting shifts created, employees invited) and produce the `trial_goals` table.

- **Data Marts Layer**:  
  The final `trial_activation` table is created, which shows organizations that have completed all trial goals.

---

### **3. Visualization**

Lastly, dashboards or charts can be created using tools like **Power BI**, **Tableau**, or **Looker** to provide insights into trial activations and goal completion.


