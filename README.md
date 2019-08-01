# Pollinator
An airflow infrastructure project generation tool.

## Airflow Data Platform Generation Tool 

Here at BrightHive we embrace the constant need to spin up data pipeline infrastructure for our clients with speed and security. Recently, we adopted Airflow into our infrastructure. Through our trial and errors, along with a gigantic amount of research, we found a few ways to configure airflow to fit our varying client needs. With this insight, we decided to make our lives easier, and yours, by automating this process and creating a generalized and simple tool that can create an Airflow platform to build etl pipelines using DAG's, along with users and permissions.



Pollinator provides an open sourced python configuration framework for builing customized airflow platform for data engineering infrastructure. This is useful when:
 * You need to create multiple airflow platform projects on the fly
 * Have the need to set up user permission management
 * Want to deploy a new airflow platform but without the headache of parsing through tons of Airflow documentation.

Pollinator is a easy, simple, and intuitive airflow based data engineering platform generator for rapid data engineering infrastructure needs.

Key Features:

- Configuration-Based: 

- Flexible:

- Direct:

- Deployable:


### How To Install

```
git clone ...
make install
```

### How To Use

#### Create a configuration file
```
{
    "platform":{
        "name": "<PLATFORM_NAME>",
        "executor": "celery",
        "include_files": true,
        "include_hive": true,
        "include_aws": true,
        "include_examples": true,
        "include_pollinator_dags": true
    },
    "aws": {
        "access_key_id": "<ACCESS_KEY_ID>",
        "secret_access_key": "<SECRET_ACCESS_KEY>"
    },
    "postgres" : {
        "user": "airflow",
        "password": "airflow",
        "port": 5439
    },
    "airflow": {
        "email": {
            "email_address": "<AIRFLOW_EMAIL_ADDRESS>",
            "password": "<EMAIL_PASSWORD>",
            "smtp_host": "smtp.google.org",
            "smtp_port": 587
        },
        "users":[
            {
                "firstname": "<FIRST_NAME>",
                "lastname": "<LAST_NAME>",
                "email_address": "<USER_EMAIL>",
                "password": "<LOGIN_PASSWORD>"
            }
        ]
    }
}
```

```
cd path/to/project/dir 
pollinator
```
