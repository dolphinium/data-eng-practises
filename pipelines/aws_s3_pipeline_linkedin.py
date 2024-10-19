from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME_LINKEDIN
import os

def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='linkedin_extraction', key='return_value')
    s3 = connect_to_s3()
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME_LINKEDIN)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME_LINKEDIN, file_path.split('/')[-1])