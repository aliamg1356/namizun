from setuptools import setup, find_packages

setup(name='namizun_core',
      version='1.3.8',
      description='namizun main functions',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      url='https://github.com/aliamg1356/namizun',
      packages=find_packages(include=['namizun_core', 'namizun_core.*']),
      setup_requires=['wheel'],
      install_requires=[
          'psutil==5.9.4',
          'redis==4.3.5',
          'pytz==2022.6',
      ]
      )
