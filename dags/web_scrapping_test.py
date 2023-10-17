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
    'web_scraping_dag',
    default_args=default_args,
    description='A DAG to perform web scraping with Docker',
    schedule_interval=timedelta(days=1),  # Set the frequency as needed
)

# Step 1: Build Docker Image
# build_image = DockerOperator(
#     task_id='build_image',
#     image='my_selenium_image',  # Use the name you specified in docker build
#     api_version='auto',
#     auto_remove=True,
#     command='/usr/bin/docker build -f ${AIRFLOW_PROJ_DIR}/Dockerfile-selenium -t my_selenium_image . --tag sel_webscrap',
#     docker_url='tcp://docker-socket-proxy:2375',
#     network_mode='bridge',
#     mount_tmp_dir=False,
#     dag=dag,
# )

# Step 1: Build Docker Image
# build_image = BashOperator(
#     task_id='build_image',
#     bash_command='docker build -f Dockerfile-selenium -t my_selenium_image . --tag sel_webscrap',
#     network_mode='bridge',    
#     dag=dag,
# )

# Step 2: Run Docker Container
run_container = DockerOperator(
    task_id='run_container',
    image='my_selenium_image',
    container_name='sel_webscrap',
    auto_remove=True,
    command='python3 /home/seluser/get_data.py', 
    docker_url='tcp://docker-socket-proxy:2375',
    network_mode='bridge',
    mount_tmp_dir=False,
    dag=dag,
)

# Step 3: Execute Script
# Define the execution order
run_container
# build_image >> run_container 
