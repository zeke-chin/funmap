#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyyaml>=6.0',
    'xgboost>=1.7.4',
    'numpy>=1.24.2',
    'scipy>=1.10.1',
    'pyarrow>=11.0.0',
    'pandas>=1.5.3',
    'joblib>=1.2.0',
    'matplotlib>=3.7.0',
    'seaborn>=0.12.2',
    'scikit-learn>=1.2.1',
    'imblearn>=0.10.1',
    'tqdm>=4.64.1',
    'PyPDF2>=3.0.1',
    'matplotlib_venn>=0.11.7',
    'networkx>=3.0',
    'powerlaw>=1.5',
    ]

test_requirements = [ ]

setup(
    author="Zhiao Shi",
    author_email='zhiao.shi@gmail.com',
    python_requires='>=3.7',
    description="generate gene co-function networks using omics data",
    entry_points={
        'console_scripts': [
            'funmap=funmap.cli:main',
        ],
    },
    install_requires=requirements,
    license='MIT license',
    long_description='\n\n' + history,
    include_package_data=True,
    keywords=['funmap', 'bioinformatics', 'biological-network'],
    name='funmap',
    packages=find_packages(include=['funmap', 'funmap.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bzhanglab/funmap',
    version='0.1.9',
    zip_safe=False,
)
