# Python Packages Installation in the Container

Running the following command will build a container and open a Bash shell:
```bash
docker run -it python:3.9-bookworm bash
```
Once inside the container, you should see a prompt like this:
```bash
root@3978e2e905d1:/#
```

In this mode, all standard terminal commands work fine. For instance, running `whoami` will confirm that you are logged in as `root`. You can navigate the virtual file system of the container just as if you were logged into an external computer.

Let's install `numpy` in Python! First, navigate to the `home` directory, create a folder named `mypyproject`, and enter it:
```bash
cd /home
mkdir mypyproject
cd mypyproject
```

To start a new Python project, create and activate a virtual environment. This keeps your project's dependencies isolated from the global Python environment used by Linux. Starting from Python 3.12, using a virtual environment is explicitly required:
```bash
python3 -m venv venv  # Creates a virtual environment
source venv/bin/activate  # Activates the virtual environment
```

After activating the virtual environment, you will notice the `(venv)` prefix in your terminal prompt, indicating that your terminal is now operating within this isolated environment:
```bash
(venv) root@3978e2e905d1:/home/mypyproject#
```

Now you can install `numpy` using pip:
```bash
pip install numpy
```

With `numpy` installed, you can use it in Python:
```bash
python
```
Inside the Python interpreter:
```python
import numpy as np
np.random.rand(3, 2)  # Creates a 3x2 matrix
```

## Python script
Surprisingly, a basic Linux container might not have a text editor installed. Install one, for instance `vim`.
```bash
apt-get update  # Updates the package list so the system knows which packages are available.
apt-get install vim  # If you are not familiar with VIM, make sure to learn the basics.
# Just in case, ZQ quits from VIM :)
```
Now we can execute a Python script in the usual manner. For simplicity, the script reads a vector from standard input and outputs the norm of the vector:
```python
import numpy as np

input_str = input("Enter the elements of the 1D array separated by spaces: ")
array = np.array([float(x) for x in input_str.split()])
norm = np.linalg.norm(array)
print(f"The norm of the array is: {norm}")
```
The code above should be put into a file `norm.py` and executed within the container
```bash
python /home/mypyproject/norm.py
```
Similarly, the same script can be called outside from the container.
```bash
# docker exec -it container_id Executable parameter1 parameter2
# this part needs activation of the environment
docker exec -it 3978e2e905d1 python /home/mypyproject/norm.py
```
or more explicitly
```bash
docker exec -it serene_kare bash -c "source /app/venv/bin/activate && python /home/mypyproject.py"
```



Unfortunately, any progress made within the container, such as installing numpy, creating folders, or adding files, cannot be saved into the image. This means that you cannot share your progress with colleagues because containers are not designed to be shared. But images are.
On the next page we are going to find out how to make your own image.

[Creating your own image](./Docker4.md)