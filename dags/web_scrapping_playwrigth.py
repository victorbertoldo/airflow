from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'web_scraping_playwright_dag',
    default_args=default_args,
    description='A DAG to perform web scraping with Docker',
    schedule_interval=timedelta(days=1),  # Set the frequency as needed
)

# Step : Run Docker Container
run_container = DockerOperator(
    task_id='run_container',
    image='test-playwright',
    container_name='playwright-webscrap',
    auto_remove=True,
    command='python /home/pwuser/teste_playwrite.py', 
    docker_url='tcp://docker-socket-proxy:2375',
    network_mode='bridge',
    mount_tmp_dir=False,
    dag=dag,
)

# Step 3: Execute Script
# Define the execution order
run_container
# build_image >> run_container 
