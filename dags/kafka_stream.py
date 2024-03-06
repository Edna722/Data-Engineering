import os

# Set the AIRFLOW_HOME environment variable to the directory containing your airflow.cfg file
AIRFLOW_HOME = r"C:\Users\wanji\anaconda3\envs\learn-env\Lib\site-packages\airflow"
os.environ['AIRFLOW_HOME'] = AIRFLOW_HOME

from datetime import datetime
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator  

default_args = {
    'owner':'airscholar',
    'start_date':datetime(2024, 3, 6, 13, 15) 
}
# Create a function for stream_data
def stream_data():
    import json
    import requests
    
    res = requests.get("https://randomuser.me/api/")
    print(res.json())

with DAG('user_automation',
         default_args = default_args,
         schedule_interval='@daily',
         catchup = False) as dag:
    
    streaming_task = PythonOperator(
        task_id='streaming_data_from_api',
        python_callable = stream_data
    )
stream_data();