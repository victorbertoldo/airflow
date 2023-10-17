# Here some utils to use day to day

### To see the configuration file of airflow, we have to copy from the scheduler container:

``` shell
docker cp airflow-airflow-scheduler-1:/opt/airflow/airflow.cfg .
```
> Now the file are in you current directory


### Celery
The celery executor has a kind of a monitoring that names flower. If you want to see the flower executor you need to add this to your running cluster. 

``` shell
docker compose down && docker compose --profile flower up -d
```


### Restart the cluster after changing some configuration

``` shell
docker compose down && docker compose up -d
```

### Restart the cluster with flower running

``` shell
docker compose --profile flower down && docker compose down &&docker compose --profile flower up -d
```
