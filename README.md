# Pollinator
Pollinator is a tool that rapidly generates a containerized Apache Airflow data pipeline infrastructure.

## Airflow Data Platform Generation Tool 

Pollinator provides an open sourced python configuration framework for builing customized airflow platform for data engineering infrastructure. This is useful when:
 * You need to create multiple airflow platform projects on the fly
 * Have the need to set up user permission management
 * Want to deploy a new airflow platform but without the headache of parsing through tons of Airflow documentation.

Pollinator is an easy, simple, and intuitive airflow based data engineering platform generator for rapid data engineering infrastructure needs. Pollinator simplifies the process of configuring Airflow for data pipeline infrastructure needs by providing a simplified configuration file. 


### Installation

Pollinator requires the following:
 * Python >= 3.7.3
 * Pip package manager

To check to see if you have the proper requirements, try to run:
```
python --version
pip --verion
```

To install pollinator run:
```
git clone https://github.com/brighthive/pollinator.git
cd pollinator
make install
```

### How To Use Pollinator

1. Create project directory and cd into it
```
mkdir data_project
cd data_project
```
2. Create and save the pollinator configuration file as  **config.json** using the following config template below in the project directory.

```
{
    "platform":{
        "name": "<PLATFORM_NAME>",
        "executor": "celery",
        "include_hive": true,
        "include_aws": true,
        "include_examples": true
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
        "authentication": false,
        "accounts":[
            {
                "firstname": "<FIRST_NAME>",
                "lastname": "<LAST_NAME>",
                "email": "<USER_EMAIL>",
                "password": "<LOGIN_PASSWORD>",
                "username": "<USERNAME>"
            }
        ]
    }
}
```
3. Once the config.json file has been created run the following command to initialize your data infrastructure project directory.
```
pollinator
```

4. Now that you have successfully initalized, you should now be able to start your infrastructure using the following:
```
make build
make run
```

5. To check if your infrastructure is ready, you should visit "localhost:8080".
   
6. To stop your infrastructure, run the following command:
```
CTRL+C
make stop
```