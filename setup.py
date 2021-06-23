from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Persian-Arabic Search',
    version='1.1',
    packages=[''],
    url='sinaai.github.io',
    license='',
    author='sina',
    install_requires=required,
    author_email='sinakhan@live.com',
    description=''
)