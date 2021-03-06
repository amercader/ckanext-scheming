from setuptools import setup, find_packages
import sys, os

version = '1.0.1b'

setup(
    name='ckanext-scheming',
    version=version,
    description="Easy, sharable custom CKAN schemas",
    long_description="""
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Government of Canada',
    author_email='ian@excess.org',
    url='https://github.com/ckan/ckanext-scheming',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "ckanapi",
        "ckantoolkit>=0.0.2",
        "pytz==2012j",
    ],
    entry_points=\
    """
    [ckan.plugins]
    scheming_datasets=ckanext.scheming.plugins:SchemingDatasetsPlugin
    scheming_groups=ckanext.scheming.plugins:SchemingGroupsPlugin
    scheming_organizations=ckanext.scheming.plugins:SchemingOrganizationsPlugin
    scheming_test_subclass=ckanext.scheming.tests.plugins:SchemingTestSubclass

    [paste.paster_command]
    scheming=ckanext.scheming.commands:SchemingCommand
    """,
)
