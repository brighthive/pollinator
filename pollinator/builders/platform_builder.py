import os 
import shutil
import warnings
from pollinator.config import Config
from pollinator.exceptions import PollinatorPlatformError, PollinatorPlatformBuildError, PollinatorPlatformValidationError
from pollinator.builders import PollinatorDockerDocumentBuilder, PollinatorAirflowDocumentBuilder, \
    PollinatorBuildDocumentBuilder

class PollinatorPlatformBuilder(object):

    def __init__(self, context,  overwrite=True, append=True):
        self.overwrite = overwrite
        self.append = append
        self.context = context
        self.dirty = False

    def ensure(self):
        root_dir = Config.PLATFORM_ROOT_PATH
        platform_dirs = Config.PLATFORM_DIRS

        for path in platform_dirs:
            # Check if directory can be scaffold
            if os.path.isdir(path) and not self.overwrite and not self.append:
                self.dirty = True

        if self.dirty:
            raise PollinatorPlatformBuildError('project root directory is not clean, please use clean directory')

    def scaffold(self):
        root_dir = Config.PLATFORM_ROOT_PATH
        platform_dirs = Config.PLATFORM_DIRS

        # Can't overwrite root_directory 
        if not os.path.isdir(root_dir):
            try:
                os.makedirs(root_dir)
            except (OSError):
                raise PollinatorPlatformBuildError("unable to create project context root directory")
        for path in platform_dirs:

            # If path exists and overwrite = True, overwrite
            if os.path.isdir(path) and self.overwrite and path != root_dir:
                shutil.rmtree(path)
                os.makedirs(path)
                continue
            
            # If path does not exist, create
            if not os.path.isdir(path):
                try:
                    os.makedirs(path)
                except(OSError):
                    raise PollinatorPlatformBuildError("unable to create project context root directory")
    
    def add_static_files(self, static_includes_dir=None, dest_dir=None, recursive=True):
        
        if static_includes_dir is None:
            static_includes_dir = Config.INCLUDES_DIR
        
        if not os.path.isdir(static_includes_dir):
            raise PollinatorPlatformBuildError('includes directory {} is not valid'.format(static_includes_dir))
        
        if dest_dir is None:
            dest_dir = Config.PLATFORM_ROOT_PATH

        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir)

        for file_name in os.listdir(static_includes_dir):
            file_abs_path = os.path.join(static_includes_dir, file_name)

            if os.path.isfile(file_abs_path):
                shutil.copy(file_abs_path, dest_dir)
            

            if os.path.isdir(file_name) and recursive:
                nested_dir_name = os.path.join(static_includes_dir, file_name)
                nested_dest_dir_name = os.path.join(dest_dir, file_name)
                self.add_static_files(nested_dir_name, nested_dest_dir_name)

    def build(self):
        self.ensure()
        self.scaffold()
        self.add_static_files()
        
        docker_document_builder = PollinatorDockerDocumentBuilder(self.context)
        docker_document_builder.build()

        airflow_document_builder = PollinatorAirflowDocumentBuilder(self.context)
        airflow_document_builder.build()

        build_document_builder =  PollinatorBuildDocumentBuilder(self.context)
        build_document_builder.build()