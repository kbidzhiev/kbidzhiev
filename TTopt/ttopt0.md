# Tensor Network optimiser

In the current series of articles, I describe step-by-step giude on designing an SDK around a scientific software package. As an example, I have chosen the [Tensor Train Optimiser (TTOpt)](https://github.com/AndreiChertkov/ttopt), in particular, this [use case](https://github.com/AndreiChertkov/ttopt/blob/master/demo/qtt_100d.py). The user can input a function, that accepts a multidimensional array as input and returns a scalar value, in other words a single number.

```math
f: \mathbb{R}^d \rightarrow \mathbb{R}
\rm{min}_X \ f(X)
```


The SDK is meant to be used as a simplified interface between the user and TTNopt application.

Input from the user:
- `rank`: Rank of the tensor network approximation. Exmaple `rank = 4`.
- `d`: Dimension of the function.
- `f`: Function for minimization. Example: `np.sum(np.abs(X * np.sin(X) + 0.1 * X), axis=1)`
- `grid_lower_bound`: Grid lower bound (number or list of length `d`). Example: `grid_lower_bound=-10.0` or `grid_lower_bound=[1, 2.2, 7, -3, ...]`
- `grid_upper_bound`: Grid upper bound (number or list of length `d`), similar to `grid_lower_bound`. Example: `grid_upper_bound=10.0`
- `p`, `q`: The grid size factor. A grid has `p^q` points. Example: `p=2`, `q=12`
- `evals`: Number of function evaluations. Example: `evals=1.E+5`
- `name`: Function name in output logs, optional. Example: `name='Alpine'`

#####






[Page 1. Creating a python SDK package](./ttopt1.md)