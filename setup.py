from setuptools import setup,find_packages

setup( 
    name="calculator",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    description="A calculator with basic operators",
    long_description=open("README.md").read(),
    url="https://github.com/AneleMaphalala/basiccalculator.git",
    author="Anele Maphalala",
    author_email="maphalalaanele@gmail.com"
    )
   