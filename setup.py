# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
      name='tempmom',
      version='1.0.0',
      author='Bjørn T. Svendsen',
      author_email='bjorn.thomas.svendsen@gmail.com',
      description='Implementation of temporal moments',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='',
      packages=find_packages(),
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
      install_requires=['numpy'],
      python_requires='>=3.7',
      )
