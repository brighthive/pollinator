import os
import json
from datetime import date
from pollinator.config import Config
from pollinator.exceptions import PollinatorContextError

class PollinatorEnvironment(object):
    BASE_AIRFLOW_MODULES = ["postgres", "crypto", "mysql", "ssh"]
    CELERY_AIRFLOW_MODULES = ["celery"]
    HIVE_AIRFLOW_MODULES = ["hive", "jdbc"]

    CELERY_EXECTOR = 'CeleryExecutor'
    LOCAL_EXECUTOR = 'LocalExecutor'

    def __init__(self, platform_config):
        self._platform_config = platform_config

    def get_platform_property(self, property_name):
        return self._platform_config.get_property(property_name, 'platform')
    
    def get_docker_property(self, property_name):
        return self._platform_config.get_property(property_name, 'docker')    
    
    def get_airflow_property(self, property_name):
        return self._platform_config.get_property(property_name, 'airflow') 

    @property
    def platform_name(self):
        return self.get_platform_property('name')
    
    @property
    def platform_executor(self):
        platform_config_executor = self.get_platform_property('executor')

        if platform_config_executor is 'local' or platform_config_executor is 'LocalExecutor':
            return self.LOCAL_EXECUTOR
        
        if platform_config_executor is 'celery' or platform_config_executor is 'CeleryExecutor':
            return self.CELERY_EXECTOR

    @property
    def is_hive_included(self):
        return self.get_platform_property('include_hive')
    
    @property
    def is_aws_included(self):
        return self.get_platform_property('include_aws')
    
    @property
    def is_extra_files_included(self):
        return self.get_platform_property('include_extra_files')
    
    @property
    def is_examples_included(self):
        return self.get_platform_property('include_examples')
    
    @property
    def is_pollinator_dags_included(self):
        return self.get_platform_property('include_pollinator_dags')
    
    @property
    def user(self):
        return self.get_airflow_property("user")

    @property
    def email_address(self):
        return self.get_airflow_property("email")["email_address"]
    
    @property
    def email_password(self):
        return self.get_airflow_property("email")["password"]
    
    @property
    def airflow_smtp_host(self):
        return self.get_airflow_property("email")["smtp_host"]
    
    @property
    def airflow_smtp_port(self):
        return self.get_airflow_property("email")["smtp_port"]

    @property 
    def airflow_home(self):
        return self.get_docker_property('airflow_home')

    @property
    def included_submodules(self):
        return self.get_docker_property('airflow_submodules')
    
    @property
    def user_accounts(self):
        return self.get_airflow_property('users')
    
    @property
    def webserver_port(self):
        return self.get_airflow_property("airflow.webserver.container.port")
        
    @property
    def postgres_port(self):
        return self.get_airflow_property('airflow.postgres.container.port')
    
    @property
    def airflow_authentication_user(self):
        return self.get_airflow_property('airflow.authentication.user')

    @property
    def airflow_authentication_email(self):
        return self.get_airflow_property('airflow.authentication.email')
    
    @property
    def airflow_authentication_password(self):
        return self.get_airflow_property('airflow.authentication.password')
    
    @property
    def airflow_rabbitmq_host(self):
        return self.get_airflow_property('airflow.rabbitmq.host')
    
    @property
    def airflow_rabbitmq_port(self):
        return self.get_airflow_property('airflow.rabbitmq.port')

    @property
    def docker_name(self):
        return self.get_platform_property("name") + "_airflow"

    @property 
    def airflow_db_host_port(self):
        return self.get_platform_property("airflow.postgres.host.port")

    @property
    def airflow_db_container_port(self):
        return self.get_platform_property("airflow.postgres.container.port")
    
    @property
    def airflow_webserver_host_port(self):
        return self.get_platform_property("airflow.webserver.host.port")
    
    @property
    def airflow_webserver_container_port(self):
        return self.get_platform_property("airflow.webserver.container.port")

    @property
    def airflow_submodules(self):
        combined_modules_list = self.BASE_AIRFLOW_MODULES
        if self.is_hive_included:
            combined_modules_list.extend(self.HIVE_AIRFLOW_MODULES)

        if self.included_submodules is not None:
            combined_modules_list.extend(self.included_submodules)

        if self.platform_executor == self.CELERY_EXECTOR:
            combined_modules_list.extend(self.CELERY_AIRFLOW_MODULES)

        return combined_modules_list