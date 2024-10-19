import pandas as pd

from etls.linkedin_etl import extract_jobs, transform_data, load_data_to_csv
from utils.constants import OUTPUT_PATH

def linkedin_pipeline(file_name: str, config_file= 'config.json'):
    # extraction
    jobs_list = extract_jobs(config_file) # manage config file
    jobs_df = pd.DataFrame(jobs_list)
    # transformation
    jobs_df = transform_data(jobs_df)
    # load to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(jobs_df, file_path)