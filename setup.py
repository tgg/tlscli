from distutils.core import setup

setup(
    name='tlscli',
    version='0.8.0',
    author='Thomas Girard',
    author_email='thomas.g.girard@free.fr',
    url='http://pypi.python.org/pypi/tlscli/',
    license='LICENSE.txt',
    description='Text User Interface client for CORBA Telecom Log Service.',
    long_description=open('README.txt').read(),
    scripts=['tlscli'],
    data_files=['DsLogAdmin.idl'],
    requires=['omniidl.main']
)
