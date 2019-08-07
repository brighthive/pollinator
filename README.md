# Pollinator
Pollinator is a tool that rapidly generates a containerized Apache Airflow data pipeline infrastructure.

## Airflow Data Platform Generation Tool 

Pollinator provides an open sourced python configuration framework for builing customized airflow platform for data engineering infrastructure. This is useful when:
 * You need to create multiple airflow platform projects on the fly
 * Have the need to set up user permission management
 * Want to deploy a new airflow platform but without the headache of parsing through tons of Airflow documentation.

Pollinator is an easy, simple, and intuitive airflow based data engineering platform generator for rapid data engineering infrastructure needs. Pollinator simplifies the process of configuring Airflow for data pipeline infrastructure needs by providing a simplified configuration file. 


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
        "include_hive": true,
        "include_aws": true,
        "include_examples": true,
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
                "password": "<LOGIN_PASSWORD>",
                "role" : "admin"
            }
        ]
    }
}
```

```
cd path/to/project/dir 
pollinator
```
