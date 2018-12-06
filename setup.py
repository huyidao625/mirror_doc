#coding=utf-8
#!/usr/bin/env python
#python 2.7.5
#author: hufei
try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup
    
setup(
      name="mirror",
      version='1.6.7a7',
      author="mirror group",
      packages=find_packages(),
      description="1.6.7a7",
      install_requires=[
          'sphinx_nameko_theme',
          'nameko',
          'mirror_logstash',
          'Cheetah3',
          'DBUtils',
          'elasticsearch_dsl',
          'elasticsearch',
          'fs',
          'kazoo',
          'netifaces',
          'pika',
          'psutil',
          'pyftpdlib',
          'PyMySQL',
          'PyYAML',
          'redis',
          'xlrd'
          ],
      zip_safe=True
      )