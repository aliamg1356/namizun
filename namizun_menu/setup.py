from setuptools import setup, find_packages

setup(name='namizun_menu',
      version='1.3.8',
      description='namizun menu',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      url='https://github.com/malkemit/namizun',
      packages=find_packages(include=['namizun_menu', 'namizun_menu.*']),
      setup_requires=['wheel'],
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']
      )
