from setuptools import setup

setup(
   name='Amazon',
   version='0.0.1',
   author='Marwan Sultan',
   author_email='Marwan.Sultan@gmail.com',
   packages=['amazon.functions', 'amazon.tests', 'amazon.data'],
   scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='Executing data driven and API testing',
   long_description=open('README.txt').read(),
   install_requires=[
       "pytest",
   ],
)