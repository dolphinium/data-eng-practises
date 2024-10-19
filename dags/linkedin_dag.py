from datetime import datetime 
import os
import sys

from airflow import DAG # type: ignore
from airflow.operators.python import PythonOperator # type: ignore


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.linkedin_pipeline import linkedin_pipeline
from pipelines.aws_s3_pipeline_linkedin import upload_s3_pipeline

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
        'config_file': 'config.json'
    },
    dag=dag
)


# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload_linkedin',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3

