from setuptools import setup, find_packages
import os
from io import open


# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Name of the package
    name='helpers',

    

    # Start with a small number and increase it with every change you make
    # https://semver.org
    version='1.0.1',

    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    # For example: MIT
    license='',

    # Short description of your library
    description='Out custom collection of helper functions and variables',

    # Long description of your library
    long_description = long_description,
    # long_description_context_type = 'text/markdown',

    # Your name
    author='ssanga', 

    # Your email
    author_email='',     

    # Either the link to your github or to your website
    url='',

    # Link from which the project can be downloaded
    download_url='',

    # List of keyword arguments
    keywords=[],

    # List of packages to install with this one
    install_requires=[],

    # https://pypi.org/classifiers/
    classifiers=[],  

    package_dir={'src':'src'},

    # Packages to include into the distribution
    packages=find_packages('.'), 
    # packages=find_packages(where='src')
     
)

# pip install --upgrade wheel
# E:\TFS\Github\PCAP\src\03_modules-and-packages\helpers> python setup.py --commands
# E:\TFS\Github\PCAP\src\03_modules-and-packages\helpers> python setup.py bdist_wheel
# E:\TFS\Github\PCAP\src\03_modules-and-packages\helpers> pip install E:\TFS\Github\PCAP\src\03_modules-and-packages\helpers\dist\helpers-1.0.0-py3-none-any.whl
# E:\TFS\Github\PCAP> pip uninstall -y helpers
# E:\TFS\Github\PCAP\src\03_modules-and-packages\helpers> pip install --editable .
