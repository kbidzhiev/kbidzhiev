import numpy as np

def create_function_from_input(input_str):
    def f(X):
        return eval(input_str)
    return f

# Example terminal input string
terminal_input = "np.sum(np.abs(X * np.sin(X) + 0.1 * X), axis=1)"

# Create the function
f = create_function_from_input(terminal_input)

# Test the created function
X = np.array([[1, 2, 3], [4, 5, 6]])
result = f(X)
print(result)