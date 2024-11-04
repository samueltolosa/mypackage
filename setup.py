from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],  # Correct spelling and case
    url='https://github.com/samueltolosa/samueltolosa/edit/main/README.md',
    author='Samuel Tolosa',
    author_email='samueltolosaa@gmail.com'
)
