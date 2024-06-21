# Python Packages Installation in the Container

Running the following command will start a container and open a Bash shell:
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
