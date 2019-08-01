import os
from jinja2 import Environment, FileSystemLoader
from datetime import date
from pollinator.config import Config
from pollinator.builders import PollinatorDocumentBuilder

class PollinatorDockerDocumentBuilder(PollinatorDocumentBuilder):

    def __init__(self, environment):
        self.environment = environment
        self.templates_dir = Config.DOCKER_TEMPLATES_DIR
        self.output_dir = Config.PLATFORM_ROOT_PATH
        super().__init__(self.environment,  self.output_dir, self.templates_dir,)
