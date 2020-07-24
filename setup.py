import codecs

from setuptools import find_packages, setup

setup(name='gapipy',
    description='A wrapper for the Google Analytics API. Originally maintained by Stijn Debrouwere. Now maintained by Huw Fulcher.',
    long_description=codecs.open('README.md', 'r', 'utf-8').read(),
    author='Huw Fulcher',
    author_email='fulcherhuw@gmail.com',
    url='https://github.com/huwfulcher/gapipy/',
    download_url='http://www.github.com/huwfulcher/gapipy/tarball/master',
    version='0.26.0',
    license='ISC',
    packages=find_packages(),
    keywords='data analytics api wrapper google',
    include_package_data=True,
    install_requires=[
        'google-auth>=1.19.2',
        'google-api-python-client>=1.10.0',
        'google-auth-oauthlib>=0.4.1'
        'python-dateutil',
        'addressable>=1.4.2',
        'inspect-it>=0.3.2',
        'werkzeug>=1.0.1',
        'click>=7.1.2',
        'pyyaml>=5.3.1',
        'prettytable>=0.7.2',
        'colorama>=0.4.3',
        'snakify>=1.1',
        'python-dotenv>=0.14.0'
    ],
    test_suite='gapipy.tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        ],
    )
