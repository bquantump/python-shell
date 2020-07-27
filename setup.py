  
from setuptools import setup

setup(
    name='python-shell',
    version="0.1",
    description='Python embeded shell',
    long_description="",
    license='MIT',
    author='Microsoft Corporation',
    author_email='azpycli@microsoft.com',
    url='https://github.com/bquantump/python-shell',
    zip_safe=False,
    classifiers=["Programming Language :: Python :: 3"],
    packages=['pyshell'],
    install_requires=['pytest'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['pyshell=pyshell.runner:main']
    }
)