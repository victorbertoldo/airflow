Concurrency, the parameters you must know!

#### Concurrency, the parameters you must know!

Airflow has several parameters to tune your tasks and DAGs concurrency.

**Concurrency** defines the number of tasks and DAG Runs that you can execute at the same time (in parallel)

  

_Starting from the configuration settings_

**parallelism / AIRFLOW\_\_CORE\_\_PARALELISM**

This defines the maximum number of task instances that can run in Airflow per scheduler. By default, you can execute up to 32 tasks at the same time. If you have 2 schedulers: 2 x 32 = 64 tasks.

What value to define here depends on the resources you have and the number of schedulers running.

  

**max\_active\_tasks\_per\_dag / AIRFLOW\_\_CORE\_\_MAX\_ACTIVE\_TASKS\_PER\_DAG**

This defines the maximum number of task instances allowed to run concurrently in each DAG. By default, you can execute up to 16 tasks at the same time for a given DAG across all DAG Runs.

  

**max\_active\_runs\_per\_dag / AIRFLOW\_\_CORE\_\_MAX\_ACTIVE\_RUNS\_PER\_DAG**

This defines the maximum number of active DAG runs per DAG. By default, you can have up to 16 DAG runs per DAG running at the same time.