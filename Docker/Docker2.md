# Your first [Python container](https://hub.docker.com/_/python)

After following the link, you will find many different versions of Python, such as 3.12, 3.9, etc. Which one should you choose? Additionally, terms like 'Alpine,' 'Bookworm,' and 'Bullseye' refer to different versions of Linux. Alpine is considered extremely lightweight, while Bookworm and Bullseye are versions of Debian (cousin of Ubuntu)." I randomly select "bookworm" python 3.9.19 and click on the [link](https://github.com/docker-library/python/blob/1b7a1106674a21e699b155cbd53bf39387284cca/3.9/bookworm/Dockerfile), which brings me to the *Dockerfile*. 

## Dockerfile
A Dockerfile is a text file that contains instructions on how Docker should build a container. Here's what typically goes inside it:

- `FROM`: This directive specifies the base image to use for the Docker container. For example, we use buildpack-deps:bookworm as our starting point.
- `RUN`: This command executes during the building phase of the container. With RUN, you can install packages, copy files from your computer to the container, or perform other setup tasks.
- `ENV`: This sets environment variables within the container, similar to how the env command works in Linux. It can define things like the location of Python, your username, and more.
- `CMD`: This specifies the command that runs when the container starts. It acts as the entry point of the container. In our example, the container starts with CMD ["python3"]. The syntax CMD ["executable", "parameter1", "parameter2", ...] mirrors how you would run a command in a terminal, such as python3 myscript.py -i inputfile.txt.

These elements together define how the Docker container is built and what it does when it runs.