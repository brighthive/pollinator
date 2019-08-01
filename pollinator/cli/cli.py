import os
import click
from pollinator.config import Config
from pollinator.app import App

HELP_TEXT = 'Pollinator is a configuration based airflow data engineering platform generator. This is version {} .'.format(Config.VERSION)

@click.command(help=HELP_TEXT)
@click.version_option(Config.VERSION, message='%(version)s' )
@click.option('--config', help='Path to configuration file used to generate data platform.', default=Config.PLATFORM_BASE_CONFIG_PATH, type=click.Path(exists=True) )
def cli(config):
    click.echo('Welcome to pollinator {}'.format(Config.VERSION))
    config_file_path = click.format_filename(config)
    click.echo('Using file at {} to generate airflow data platform.'.format(config_file_path))

    # Generate platform
    app = App(config_file_path)
    app.run()