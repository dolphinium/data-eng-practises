from datetime import datetime 
import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.linkedin_pipeline import linkedin_pipeline


default_args= {
    'owner': 'Yunus Emre KORKMAZ',
    'start_date': datetime(2024,10,13)
}


file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id = 'etl_linkedin_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['linkedin','etl','pipeline']
)

# extraction from linkedin
extract = PythonOperator(
    task_id='linkedin_extraction',
    python_callable=linkedin_pipeline,
    op_kwargs={
        'file_name': f'linkedin_{file_postfix}',
        'config_file':'test'
    },
    dag=dag
)

# upload to s3 part will be done later

