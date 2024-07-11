# Designing an SDK for TTopt

Lets first design a small Python package **template** of the following structure
```
ttoptSDK/
├── ttoptSDK/
│   ├── __init__.py
│   └── sdk.py
├── tests/
│   ├── __init__.py
│   └── test_sdk.py
└── setup.py
```

I put the actual code in the `sdk.py`. In the file `test_sdk.py` I write a set of tests to check the code in the `sdk.py`.

Python technical files `__init__.py` are left empty.
In the `setup.py` we put minimal required info:
```python
# setup.py
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

In the main file `sdk.py` I gather all the parameters
```python
# sdk.py
def f(X):                   # Target function
    return np.sum(np.abs(X * np.sin(X) + 0.1 * X), axis=1)

def optimize(
    rank,
    d,
    f,
    lower_grid_bound,
    upper_grid_bound,
    p_grid_factor,
    q_grid_factor,
    n_evals,
    name='Alpine',
    x_opt_real=None,
    y_opt_real=None
    ):

    tto = TTOpt(
    f=f,
    d=d,
    a=lower_grid_bound,
    b=upper_grid_bound,
    p=p_grid_factor,
    q=q_grid_factor,
    evals=n_evals,
    name=name,
    x_opt_real=x_opt_real,
    y_opt_real=y_opt_real,
    with_log=True)

    tto.optimize(rank)

    x_min = tto.x_opt
    y_min = tto.y_opt
    n_chache_usage = tto.k_cache
    n_requests = tto.k_total
    t_average = tto.t_evals_mean

    assert tto.k_evals == n_evals

    return x_min, y_min, (n_chache_usage, n_func_requests, t_average)
```
