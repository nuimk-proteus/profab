import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "profab",
    version = "0.4.1",
    author = "Proteus Technologies Infrastructure team",
    author_email = "infrastructure@proteus-tech.com",
    url = 'https://github.com/Proteus-tech/profab',
    description = ("Automated tools for engaging with server infrastructure on AWS"),
    long_description = read('README.markdown'),
    license = "Boost Software License - Version 1.0 - August 17th, 2003",
    keywords = "devops ec2 fabric boto",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved",
    ],
    packages = ['profab', 'profab.role',
        'profab.role.ami', 'profab.role.munin'],
    scripts = [
        'bin/pf-server-list', 'bin/pf-server-role-add',
        'bin/pf-server-start', 'bin/pf-server-terminate', 'bin/pf-server-upgrade'],
    install_requires = ['simplejson', 'fabric >= 1.2.0', 'boto >= 2.0'],
    dependency_links = [
        'git://github.com/boto/boto.git'],
)
