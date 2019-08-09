import os
import sys
import configparser
import json 
from cryptography.fernet import Fernet

DEFAULT_FERNET_KEY = Fernet.generate_key().decode()

def get_version():
    version = None
    try:
        version = open(os.path.join(sys._MEIPASS, 'VERSION')).read().strip()
    except AttributeError:
        version = open(os.path.join(os.path.dirname(__file__), '..', 'VERSION')).read().strip()
    return version

def get_relative_path():
    return os.path.relpath(os.path.join(os.path.dirname(__file__), '..'))

def get_absolute_path():
    return os.path.dirname(os.path.dirname(__file__))

def get_root_path():
    return get_absolute_path().split(os.path.dirname(__file__))[0]

def get_platform_root_path():
    return os.path.abspath(os.curdir)

def get_default_platform_config_file_path():
    return os.path.join(os.path.dirname(__file__), 'default_config.json')

def get_platform_config_path():
    return os.path.join(get_platform_root_path(), 'config.json')

def get_templates_dir_path():
    return os.path.join(get_absolute_path(), 'templates' )

def get_include_files_dir_path():
    return os.path.join(get_absolute_path(), 'include')

class Config:
    """
        Base configuration class.

        Class Attributes: 
            VERSION (str): Current version
    """

    FERNET_KEY = DEFAULT_FERNET_KEY
    VERSION = get_version()
    RELATIVE_PATH = get_relative_path()
    ABSOLUTE_PATH = get_absolute_path()
    ROOT_PATH = get_root_path()

    TEMPLATES_DIR = get_templates_dir_path()
    AIRFLOW_TEMPLATES_DIR = os.path.join(TEMPLATES_DIR, 'airflow')
    DOCKER_TEMPLATES_DIR = os.path.join(TEMPLATES_DIR, 'docker')
    BUILD_TEMPLATES_DIR = os.path.join(TEMPLATES_DIR, 'build')

    INCLUDES_DIR = get_include_files_dir_path()
    DOCKER_INCLUDES = os.path.join(INCLUDES_DIR, "docker")
    AIRFLOW_INCLUDES = os.path.join(INCLUDES_DIR, "airflow")
    BIN_INCLUDES = os.path.join(INCLUDES_DIR, "bin")


    PLATFORM_DEFAULT_CONFIG_PATH = get_default_platform_config_file_path()
    PLATFORM_BASE_CONFIG_PATH = get_platform_config_path()

    PLATFORM_ROOT_PATH = get_platform_root_path()
    PLATFORM_BIN_PATH = os.path.join(PLATFORM_ROOT_PATH, 'bin')
    PLATFORM_AIRLFOW_PATH = os.path.join(PLATFORM_ROOT_PATH, 'airflow')
    PLATFORM_AIRLFOW_DAGS_PATH = os.path.join(PLATFORM_AIRLFOW_PATH, 'dags')
    PLATFORM_AIRLFOW_LOGS_PATH = os.path.join(PLATFORM_AIRLFOW_PATH, 'logs')
    PLATFORM_AIRLFOW_PLUGINS_PATH = os.path.join(PLATFORM_AIRLFOW_PATH, 'plugins')
    PLATFORM_DOCKER_SUB_PATH = os.path.join(PLATFORM_ROOT_PATH, 'docker')

    PLATFORM_DIRS = [
        PLATFORM_AIRLFOW_PATH,
        PLATFORM_AIRLFOW_DAGS_PATH,
        PLATFORM_AIRLFOW_LOGS_PATH,
        PLATFORM_AIRLFOW_PLUGINS_PATH,
        PLATFORM_BIN_PATH    
    ]

    def __init__(self):
        self.aws_profile = 'default'
        
        self.postgres_service_name = 'postgres'
        self.postgres_service_host = 'localhost'
        self.postgres_host = 'postgres'
        self.postgres_user = 'airflow'
        self.postgres_password = 'airflow'
        self.postgres_port = 5432

        self.airflow_scheduler_service_name = 'scheduler'
        self.airflow_port = 8080
        self.PLATFORM_CONFIG_PATH = get_platform_config_path()

    def get_aws_credentials(self, profile_name=None):
        if profile_name is None:
            profile_name = self.aws_profile

        aws_dir = os.path.join(os.environ["HOME"], ".aws")

        # Get AWS access_key_id and secret_access_key from credentials file
        credentials_path = os.path.join(aws_dir, "credentials")
        credentials = configparser.ConfigParser()
        credentials.read(credentials_path)

        assert profile_name in credentials.sections()

        access_key_id = credentials[profile_name]["aws_access_key_id"]
        secret_access_key = credentials[profile_name]["aws_secret_access_key"]
        # Get AWS region and output from config file
        config_path = os.path.join(aws_dir, "config")
        config = configparser.ConfigParser()
        config.read(config_path)

        assert profile_name in config.sections()

        region = config[profile_name]['region']
        output = config[profile_name]['output']

        return {
                'access_key_id': access_key_id, 
                'secret_access_key': secret_access_key,
                'region': region,
                'output': output
                }

