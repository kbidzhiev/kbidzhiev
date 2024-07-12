# Tensor Network optimiser

In the current series of articles, I describe step-by-step guide on designing an SDK around a scientific software package. Some steps continue and reiterate part of ["Docker from zero to hero"](../Docker/Docker1.md).

As an example of a scientific software, I have chosen the [Tensor Train Optimiser (TTOpt)](https://github.com/AndreiChertkov/ttopt), in particular, this [use case](https://github.com/AndreiChertkov/ttopt/blob/master/demo/qtt_100d.py). We focus on the optimisation of multidimensional functions.

```math
f: \mathbb{R}^d \rightarrow \mathbb{R}
\rm{min}_X \ f(X)
```


The SDK is meant to be used as a simplified interface between the user and TTopt application.

### Input from the user
`function` to optimise and a `domain of search` for minima should be specified by user

Detailed description of the input parameters:
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
Optimizer returns 3 values -- `x_min, y_min, search_info`:
```python
x_min, y_min, search_info = optimize(...)
```
- `x_min`: The found argument of the minimum 
- `y_min`: The found value of the minimum of the function y_min=f(x_min).
The field `search_info` has
- `search_info.n_chache_usage`: Total number of cache usage
- `search_info.t_average`: Average time spent to real function call for 1 point
- `search_info.total`: Total information about search -- function_name, n_evalueations, time_all, error_x, error_y


[Page 1. Creating a python SDK package](./ttopt1.md)