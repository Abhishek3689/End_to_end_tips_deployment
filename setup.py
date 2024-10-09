from setuptools import setup, find_packages
from typing import List

def get_requirements(filename:str)->List[str]:
    with open(file=filename) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    if '-e.' in requirements:
        requirements.remove('-e.')
    return requirements

setup(
    author="Abhishek",
    name="Tips Data ML",
    author_email='abhi.gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)