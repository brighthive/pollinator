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
    
    def get_postgres_property(self, property_name):
        return self._platform_config.get_property(property_name, 'postgres') 
        
    def get_aws_property(self, property_name):
        return self._platform_config.get_property(property_name, 'aws') 

    @property
    def platform_name(self):
        return self.get_platform_property('name')
    
    @property   
    def platform_user(self):
        return self.platform_name+'_admin'
    
    @property
    def platform_group(self):
        return self.platform_name+'_group'
    
    @property
    def platform_executor(self):
        platform_config_executor = self.get_platform_property('executor')

        if platform_config_executor.lower() == 'local' or platform_config_executor.lower() == 'localexecutor':
            return self.LOCAL_EXECUTOR
        
        if platform_config_executor.lower() == 'celery' or platform_config_executor.lower() == 'celeryexecutor':
            return self.CELERY_EXECTOR

    @property
    def use_celery_executor(self):
        return self.platform_executor == self.CELERY_EXECTOR

    @property
    def include_examples(self):
        return self.get_platform_property('include_examples')
    
    @property
    def include_hive(self):
        return self.get_platform_property('include_hive')
    
    @property
    def include_aws(self):
        return self.get_platform_property('include_aws')
    
    @property
    def docker_build_version(self):
        return "1.0.0"

    @property
    def docker_build_tag(self):
        return "latest"
    
    @property
    def docker_image_name(self):
        return "brighthive/{}_airflow".format(self.platform_name)
    
    @property
    def docker_image_full_name(self):
        return "{}:{}-{}".format(self.docker_image_name, self.docker_build_version ,self.docker_build_tag)

    @property
    def aws_access_key_id(self):
        return self.get_aws_property('access_key_id')

    @property
    def aws_secret_access_key(self):
        return self.get_aws_property('secret_access_key')
        
    @property
    def aws_region(self):
        return self.get_aws_property('region')
    
    @property
    def aws_output(self):
        return self.get_aws_property('output')
    
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
    def airflow_user(self):
        return self.get_airflow_property("user")

    @property
    def airflow_email_address(self):
        if self.get_airflow_property("email") is not None:
            return self.get_airflow_property("email")["email_address"]
        return None
    
    @property
    def airflow_email_password(self):
        if self.get_airflow_property("email") is not None:
            return self.get_airflow_property("email")["password"]
        return None
    
    @property
    def airflow_smtp_host(self):
        if self.get_airflow_property("email") is not None:
            return self.get_airflow_property("email")["smtp_host"]
        return None
    @property
    def airflow_smtp_port(self):
        if self.get_airflow_property("email") is not None:
            return self.get_airflow_property("email")["smtp_port"]
        return None

    @property
    def include_airflow_email(self):
        if self.airflow_email_password is not None and self.airflow_email_address is not None:
            return self.airflow_email_address.strip() is not '' and self.airflow_email_password.strip() is not ''
        return False

    @property 
    def airflow_home(self):
        return self.get_docker_property('airflow_home')

    @property
    def airflow_dags_folder(self):
        return os.path.join(self.airflow_home, 'dags')
    
    @property
    def airflow_logs_folder(self):
        return os.path.join(self.airflow_home, 'logs')
    
    @property
    def airflow_plugins_folder(self):
        return os.path.join(self.airflow_home, 'plugins')

    @property
    def included_submodules(self):
        return self.get_docker_property('airflow_submodules')
    
    @property
    def user_accounts(self):
        return self.get_airflow_property('accounts')
    
    @property
    def airflow_webserver_port(self):
        return self.get_airflow_property("webserver_port")

    @property
    def airflow_webserver_internal_port(self):
        return self.get_airflow_property("webserver_internal_port") or self.airflow_webserver_port

    @property
    def airflow_webserver_external_port(self):
        return self.get_airflow_property("webserver_external_port") or self.airflow_webserver_port

    @property
    def postgres_host(self):
        return "postgres"

    @property
    def postgres_port(self):
        return self.get_postgres_property('internal_port') or self.get_postgres_property('port')
    
    @property
    def postgres_db(self):
        return self.get_postgres_property('db')

    @property
    def postgres_exposed_port(self):
        return self.get_postgres_property("external_port") or self.get_postgres_property('port')
    
    @property
    def postgres_user(self):
        return self.get_postgres_property('user')
    
    @property
    def postgres_password(self):
        return self.get_postgres_property('password')

    @property
    def airflow_alchemy_conn_url(self):
        return "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            self.postgres_user, self.postgres_password, self.postgres_host, self.postgres_port, self.postgres_db
        )
    
    @property
    def airflow_celery_conn_url(self):
        return "db+postgresql://{}:{}@{}:{}/{}".format(
            self.postgres_user, self.postgres_password, self.postgres_host, self.postgres_port, self.postgres_db
        )
    @property
    def docker_name(self):
        return self.get_docker_property("image_name")

    @property
    def airflow_submodules(self):
        combined_modules_list = self.BASE_AIRFLOW_MODULES
        if self.include_hive:
            combined_modules_list.extend(self.HIVE_AIRFLOW_MODULES)

        if self.included_submodules is not None:
            combined_modules_list.extend(self.included_submodules)

        if self.platform_executor == self.CELERY_EXECTOR:
            combined_modules_list.extend(self.CELERY_AIRFLOW_MODULES)

        return combined_modules_list

    @property
    def fernet_key(self):
        return Config.FERNET_KEY
    
    @property
    def include_pipfile(self):
        pipfile_path = os.path.join(Config.PLATFORM_ROOT_PATH, 'Pipfile')
        pipfile_lock_path = os.path.join(Config.PLATFORM_ROOT_PATH, 'Pipfile.lock')
        return os.path.exists(pipfile_path) and os.path.exists(pipfile_lock_path)

    @property
    def include_requirements(self):
        requirements_path = os.path.join(Config.PLATFORM_ROOT_PATH, 'requirements.txt')
        return os.path.exists(requirements_path)

    @property
    def include_authorized_users(self):
        return len(self.user_accounts) != 0 and self.get_airflow_property("authentication") 