# Tensor Network optimiser

In the current series of articles, I describe step by step how to design an SDK for scientific software. As an example, I have chosen the [Tansor Train Optimiser (TTOpt)](https://github.com/AndreiChertkov/ttopt), which features an SDK built around the minimization of a scalar function. This function accepts multidimensional data as input and returns a scalar value.

```math
f: \mathbb{R}^d \rightarrow \mathbb{R}
\rm{min}_X \ f(X)
```

Example of a usage can be found [here](https://github.com/AndreiChertkov/ttopt/blob/master/demo/qtt_100d.py).



[Page 1. Creating a python SDK package](./ttopt1.md)