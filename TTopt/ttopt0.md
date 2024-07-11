# Tensor Network optimiser

In the current series of articles, I describe step-by-step guide on designing an SDK around a scientific software package. As an example, I have chosen the [Tensor Train Optimiser (TTOpt)](https://github.com/AndreiChertkov/ttopt), in particular, this [use case](https://github.com/AndreiChertkov/ttopt/blob/master/demo/qtt_100d.py). The user inputs a function, that accepts a multidimensional array and returns a scalar value, in other words a single number.

```math
f: \mathbb{R}^d \rightarrow \mathbb{R}
\rm{min}_X \ f(X)
```


The SDK is meant to be used as a simplified interface between the user and TTopt application.

### Input from the user:
- `rank`: Rank of the tensor network approximation. Example: `rank = 4`.
- `d`: Dimension of the function. Example: `d = 100`
- `f`: Function for minimization. Example: `np.sum(np.abs(X * np.sin(X) + 0.1 * X), axis=1)`
- `lower_grid_bound`: Grid lower bounds for every dimension (number or list of length `d`). If a number is given, then this value will be used for each dimension. Example: `grid_lower_bound=-10.0` or `grid_lower_bound=[1, 2.2, 7, -3, ...]`
- `upper_grid_bound`: Grid upper bounds for every dimension (number or list of length `d`). If a number is given, then this value will be used for each dimension , similar to `grid_lower_bound`. Example: `grid_upper_bound=10.0`
- `p_grid_factor`, `q_grid_factor`: The grid size factors. A grid has `n = p^q` points. Example: `p_grid_factor=2`, `q_grid_factor=12`
- `n_evals`: Number of function evaluations. Example: `n_evals=1.E+5`
- `name`: Function name in output logs, optional. Example: `name='Alpine'`
- `x_opt_real`: Anticipated real coordinates of the result (x) for the minima (list of length `d`). Optional. If this value is specified, it will be used to display the current approximation error within the algorithm iterations. Convenient for debugging and testing
- `y_opt_real`: Anticipated real value of the result (y = f(x)) for the minima (single floating number). Optional. If this value is specified, it will be used to display the current approximation error within the algorithm iterations. Convenient for debugging and testing

### Output
Optimizer returns 3 values:
```python
x_min, y_min, convergence_info = optimize(...)
```
- `x_min`: The found value of the minimum of the function
- `y_min`: The found value of the minimum of the function y_min=f(x_min).
`convergence_info` has
- `convergence_info.n_chache_usage`: Total number of cache usage
- `convergence_info.n_requests`: Total number of requests (n_chache_usage + n_func_requests)
- `convergence_info.t_average`: Average time spent to real function call for 1 point


[Page 1. Creating a python SDK package](./ttopt1.md)