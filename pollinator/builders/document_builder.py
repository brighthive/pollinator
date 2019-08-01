from pollinator.config import Config
from pollinator.exceptions import PollinatorDocumentBuilderError
from jinja2 import Environment, FileSystemLoader

import os 

class PollinatorDocumentBuilder(object):
    def __init__(self, environment, output_dir, templates_dir=None):
        self.environment = environment
        self.output_dir = output_dir
        
        if templates_dir is None:
            self.templates_dir = Config.TEMPLATES_DIR
        
        # Verify templates_dir 
        if not os.path.isdir(self.templates_dir):
            raise PollinatorDocumentBuilderError("templates directory is not a path")
        if not os.path.isdir(self.output_dir):
            raise PollinatorDocumentBuilderError("templates output path is a not a diretory ")

        # Create a Jinja Env 
        self.template_env = Environment( loader = FileSystemLoader(self.templates_dir) )

    def build(self):
        for subdir, dirs, files in os.walk(self.templates_dir):
            for file_name in files:
                dest_file_name = file_name.split('-template.j2')[0]
                template_path = os.path.join(subdir, file_name)
                output_file_name = os.path.join(self.output_dir, dest_file_name)
                template = self.template_env.get_template(file_name)
                with open(output_file_name, 'w') as fh:
                    fh.write(template.render(
                        environment=self.environment
                    ))