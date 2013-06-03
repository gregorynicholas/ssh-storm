import sys

from distutils.core import setup

setup(
    name='ssh-storm',
    version='0.3.5',
    packages=['storm'],
    url='http://github.com/emre/storm',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='Management commands to ssh config files.',
    scripts=[
        'storm/bin/ssh-storm'
    ],
    install_requires=list(filter(None, [
        "paramiko",
        "manage.py",
        "termcolor",
        "argparse" if sys.version_info[:2] < (2, 7) else None,
    ])),)
