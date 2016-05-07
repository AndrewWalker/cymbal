from setuptools import setup, find_packages
import os


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    contents = open(path).read()
    return contents


setup(
    name         = "cymbal",
    version      = "1.0.0",
    description  = "Helps you add functionality missing from libclang Python bindings",
    long_description = read('README.rst'),
    author       = "Andrew Walker",
    author_email = "walker.ab@gmail.com",
    maintainer   = "Andrew Walker",
    maintainer_email = "walker.ab@gmail.com",
    url          = "http://github.com/AndrewWalker/cymbal",
    license      = "MIT",
    packages     = find_packages(), 
    classifiers  = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
    ],
    tests_require=['unittest2'],
    test_suite='unittest2.collector'
)

