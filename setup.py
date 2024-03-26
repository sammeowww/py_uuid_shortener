from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='uuid_shortener',
    version='0.1.3',
    description='A utility to shorten UUIDs using base62 encoding.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sammeow Chan',
    author_email='1010hk@gmail.com',
    url='https://github.com/sammeowww/py_uuid_shortener',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',  # Added Python 3.12 support
    ],
    keywords='uuid shortener base62',
)

