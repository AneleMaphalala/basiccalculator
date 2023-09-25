from setuptools import setup,find_packages

setup( 
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    description="How to create a python package",
    long_description=open("README.md").read(),
    url="https://github.com/AneleMaphalala/basiccalculator.git",
    author="Anele Maphalala",
    author_email="maphalalaanele@gmail.com"
    )
   