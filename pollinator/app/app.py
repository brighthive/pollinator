from pollinator.environment import PollinatorEnvironment
from pollinator.config import Config, PollinatorConfigParser
from pollinator.builders import PollinatorPlatformBuilder
from pollinator.exceptions import PollinatorError

class App():

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
    
    def run(self):
        """
        1. Verify if current directory is clean and does not contain any conflicting files
        2. Create a platform instance from config file and verify that all required information is supplied and valid
        3. Scaffold platform directory
        4. Build platform files using templates
        """
        try:
            platform_config = PollinatorConfigParser(self.config_file_path)
            platform_environment = PollinatorEnvironment(platform_config)
            platform_builder = PollinatorPlatformBuilder(platform_environment)
            platform_builder.build()
            
        except PollinatorError as e:
            print(e.message)
