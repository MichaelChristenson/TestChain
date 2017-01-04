from setuptools import setup, find_packages

plugins = []
setup(
    name='testchain',
    version='0.0.1',
    description="""This contains unit test automation material, specifically a
                metaclass that automatically wraps testing functions""",
    long_description='',
    author='Michael Christenson',
    author_email='mochristenson@gmail.com.com',
    url='',
    install_requires=[],
    packages=find_packages(exclude=()),
    license='',
    classifiers=(
        'Development Status :: 1 - Beta',
        'Intended Audience :: Testers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5'))