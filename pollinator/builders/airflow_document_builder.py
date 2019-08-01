import os
from jinja2 import Environment, FileSystemLoader
from datetime import date
from pollinator.builders import PollinatorDocumentBuilder
from pollinator.config import Config

class PollinatorAirflowDocumentBuilder(PollinatorDocumentBuilder):
 
    def __init__(self, environment):
        self.environment = environment
        self.templates_dir = Config.AIRFLOW_TEMPLATES_DIR
        self.output_dir = Config.PLATFORM_AIRLFOW_PATH
        super().__init__(self.environment,  self.output_dir, self.templates_dir,)

