"""
setup.py serves two primary functions:
It's the file where various aspects of your project are configured. The primary feature of setup.py is that it contains a global setup() function. The keyword arguments to this function are how specific details of your project are defined. The most relevant arguments are explained in the section below.
It's the command line interface for running various commands that relate to packaging tasks. To get a listing of available commands, run python3 setup.py --help-commands.
"""



from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
   '''
   This functions will return the list of requirements
   '''
   requirements =[]
   with open(file_path) as file_obj:
      requirements = file_obj.readlines()
      requirements = [req.replace("\n","") for req in requirements]

      if HYPEN_E_DOT in requirements:
         requirements.remove(HYPEN_E_DOT)

   return requirements





setup(
name = 'mlproject',
version = '0.0.1',
author = 'Aneesha',
author_email = ' aneesham654@gmail.com',
packages = find_packages(),
#install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)