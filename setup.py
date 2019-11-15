import pathlib
from setuptools import find_packages, setup
import os

file_dir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(file_dir, 'README.md')) as f:
    long_description0 = f.read()

requirements = [
    'setuptools>=41.0.0',  # tensorboard requirements
    'fire',
    'configparser',
    'importlib'
    ]

setup(
    name="demopypackage1",  # package name for PyPI
    version="1.0.0",
    description="Demo for creating a Python package",
    long_description=long_description0,
    long_description_content_type="text/markdown",
    url="https://github.com/YUCtechlab/demopypackage1.git",    # the repo name
    author="usergkdev",
    author_email="gkuk1@hotmail.co.uk",
    license="Apache License 2.0",
    python_requires='>3.6, <4',
    classifiers=[
        "OSI Approved :: Apache Software License",
	# see; https://autopilot-docs.readthedocs.io/en/latest/license_list.html
	'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
    ],
    # packages=["a", “b”],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,       # includes non source-code files, see also manifest.in
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "trythescript=demopypackage1.__main__:main",
        ]
    },
)
