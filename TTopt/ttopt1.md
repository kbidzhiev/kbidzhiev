# Tensor Network optimiser

In the current series of articles I describe how to design an SDK around scientific software. As an example I chose the [Tansor Train Optimiser --  TTOpt](https://github.com/AndreiChertkov/ttopt) with SDK build around minimisation of a scalar function that takes as an input multidimensional data and returns a scalar 

```math
f: \mathbb{R}^d \rightarrow \mathbb{R}
\rm{min}_X \ f(X)
```