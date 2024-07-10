# Designing an SDK for TTopt

Lets first design a small Python package **template** of the following structure
```
TToptSDK/
├── TToptSDK/
│   ├── __init__.py
│   └── file_1.py
├── tests/
│   ├── __init__.py
│   └── test_of_file_1.py
└── setup.py
```

I put the actual code in the `file_1.py` and give proper name to the file and other files that appear during the code development. In the file `test_of_file_1.py` I write a set of tests to check the code in the `file_1.py` and so on.

Technical files `__init__.py` are left empty for the moment.
In the `setup.py` we put minimal required info:
```python
from setuptools import setup, find_packages

setup(
    name='ttoptSDK',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        pip install ttopt==0.6.2
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
```

