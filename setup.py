from setuptools import setup, find_packages

INSTALL_REQUIRES = []
for line in open('requirements.txt').readlines():
    requirement = line.strip()
    if requirement.startswith(('#', '-')):
        continue
    INSTALL_REQUIRES.append(requirement)

setup(
    name = 'pollinator',
    version = open('pollinator/VERSION').read().strip(),
    author = 'Amanda Crawford',
    author_email = 'amanda@brighthive.io',
    license='MIT',
    description='An opinionated airflow data engineering platform generator',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    url="https://github.com/brighthive/pollinator",
    packages = find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points = {
        'console_scripts': [
            'pollinator = pollinator.cli:cli'
        ]
    })