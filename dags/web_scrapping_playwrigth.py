from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator


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
run_container_test = DockerOperator(
    task_id='run_container_test',
    image='test-playwright',
    container_name='playwright-webscrap',
    auto_remove=True,
    command='python /home/pwuser/teste_playwright.py', 
    docker_url='tcp://docker-socket-proxy:2375',
    network_mode='bridge',
    mount_tmp_dir=False,
    dag=dag,
)


# Step 4: Execute Script
run_container_test