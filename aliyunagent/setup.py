from setuptools import setup, find_packages
import sys, os

version = '1.6'

setup(name='aliyunagent',
      version=version,
      description="ZStack aliyun agent REST service",
      long_description="""\
ZStack ECS agent REST service""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='zstack kvm python agent REST',
      author='Frank Zhang',
      author_email='xing5820@gmail.com',
      url='http://zstack.org',
      license='Apache License 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
