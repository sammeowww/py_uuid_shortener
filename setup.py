from setuptools import setup, find_packages

setup(
    name='uuid_shortener',
    version='0.1.1',
    description='A utility to shorten UUIDs using base62 encoding.',
    author='Sammeow Chan',
    author_email='1010hk@gmail.com',
    url='https://github.com/sammeowww/py_uuid_shortener',  # Git repository URL
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

