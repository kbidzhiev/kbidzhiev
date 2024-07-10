# Tensor Network optimiser

In the current series of articles, I describe step by step how to design an SDK around a scientific software package. As an example, I have chosen the [Tansor Train Optimiser (TTOpt)](https://github.com/AndreiChertkov/ttopt). 

The SDK reads a multidimensional function from the terminal and computes a minima. This function accepts multidimensional data as input and returns a scalar value:

```math
f: \mathbb{R}^d \rightarrow \mathbb{R}
\rm{min}_X \ f(X)
```

Example of a usage can be found [here](https://github.com/AndreiChertkov/ttopt/blob/master/demo/qtt_100d.py).



SDK 

[Page 1. Creating a python SDK package](./ttopt1.md)