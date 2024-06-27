# Creating your own container

As we briefly mentioned before, images are used to build containers. We have already seen an example of this on DockerHub page with the image ["python 3.9-bookworm"](https://github.com/docker-library/python/blob/1b7a1106674a21e699b155cbd53bf39387284cca/3.9/bookworm/Dockerfile) and its Dockerfile instructions for image building.

Basically I'm going to repeat what we did with numpy installation in the previous pars, but in a Dockerfile. We do that for pedagogical reasons, though there are Docker images with numpy.

A new docker image should be based on the other more "primitive" image in hierarcical sense, like a python image is based on a linux image.

```Dockerfile
FROM python:3.9-bookworm
```
The base image is set.
The next step will be to make directory for the project in our future image. For a bit more info, have a look [here](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/).

```Dockerfile
FROM python:3.9-bookworm


RUN mkdir -p /home/mypyproject
```

The command `RUN` will be executed during the build process. It allows to copy and move files form your host computer to the image.
Let's copy the `norm.py` file that contains logic that computes a norm of a 1D vector.

```Dockerfile
FROM python:3.9-bookworm

RUN mkdir -p /home/mypyproject

COPY ./norm.py /home/mypyproject/
# actually you can copy the entire folder with all the files with
# COPY ./norm.py /home/mypyproject/
```

In the `/home/mypyproject` folder, we create a virtual environment (note that modern Python requires this) and install `numpy` package to run `norm.py`. Since `RUN` command will used only once during the first bulding of the container, we can not use `RUN . /venv/bin/activate`. It will not be executed again if you stop and run the container next time. Solution to that is environmental variables `ENV`

```Dockerfile
FROM python:3.9-bookworm

RUN mkdir -p /home/mypyproject

COPY ./norm.py /home/mypyproject/

# here we define where will be located information about 
# dependent packages of out 'mypyproject'
ENV VIRTUAL_ENV=/home/mypyproject/
# here we create this location
RUN python3 -m venv $VIRTUAL_ENV
# this will tell linux to activate venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install numpy
```

After installation we can run the code

```Dockerfile
FROM python:3.9-bookworm

RUN mkdir -p /home/mypyproject

COPY ./norm.py /home/mypyproject/

ENV VIRTUAL_ENV=/home/mypyproject/

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install numpy

# Set the working directory in the container
WORKDIR /home/mypyproject
# Run the application:
CMD ["python", "norm.py"]
```

The dockerfile is ready. We can build an image from it. 
In the terminal of your computer go to the folder where `norm.py` and `Dockerfile` are and run
```bash
docker build -t vector_norm:1.0 . # -t givea a name and a version tag for your image
``` 

Congratulations ! Check `docker images` to find your image "vector_norm".
Now execute
```bash
docker run --rm -it vector_norm:1.0 # --rm removes the container after usage
```
to build a container from the image and run the python code 

Next\
[Docker page 5](./Docker5.md)

Previous\
[Docker page 3](./Docker3.md)