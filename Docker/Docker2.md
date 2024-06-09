# Your first container [BusyBox](https://en.wikipedia.org/wiki/BusyBox) - "The Swiss Army knife of Embedded Linux"

BusyBox is meant to reproduce Unix-like terminal input and output interactions.
This page is going to demonstarte how to run a basic container and check its current and previous statuses.

Firstly, to get started working, pull the container image to your system.
```bash
sudo docker pull busybox
```

output is 
```plaintext
Using default tag: latest
latest: Pulling from library/busybox
ec562eabd705: Pull complete 
Digest: sha256:9ae97d36d26566ff84e8893c64a6dc4fe8ca6d1144bf5b87b2b85a32def253c7
Status: Downloaded newer image for busybox:latest
docker.io/library/busybox:latest
```

To see what is already installed on your computer, run 
```bash
sudo docker images
```
output should be similar to
```plaintext
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
ubuntu        latest    17c0145030df   9 days ago      76.2MB
busybox       latest    65ad0d468eb1   12 months ago   4.26MB
hello-world   latest    d2c94e258dcb   13 months ago   13.3kB
```
Running the container with
```bash
sudo docker run busybox
```
displays nothing. It's similar to pressing 'enter' command in an empty shell promt. In order to see some responce, run
```bash
sudo docker run busybox echo "hello from busybox"
```
Moreover, one can get an interactive terminal with `-it` command
```bash
sudo docker run -it busybox sh
```


# Cleaning up
The command `docker run` leaves behind large files after each execution. If you do not intend to use them, please ensure they are cleaned up.

To check what remains run
```bash
sudo docker ps -a # sudo docker ps  lists active containers
```
witht he following output
```
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                        PORTS     NAMES
958b2077eca9   busybox       "sh"                     11 minutes ago   Exited (127) 10 minutes ago             condescending_bartik
98c54c4145e5   busybox       "echo 'hello from bu…"   15 minutes ago   Exited (0) 15 minutes ago               stupefied_bose
e2dec0f79a78   busybox       "sh"                     18 minutes ago   Exited (0) 18 minutes ago               nifty_dubinsky
fac40194f521   hello-world   "/hello"                 24 hours ago     Exited (0) 24 hours ago                 musing_haibt
5c4f5dd9610f   hello-world   "/hello"                 25 hours ago     Exited (0) 25 hours ago                 vigilant_kapitsa
95078a9c5748   ubuntu        "bash"                   25 hours ago     Exited (0) 25 hours ago                 kind_easley
b74e885e4a92   hello-world   "/hello"                 25 hours ago     Exited (0) 25 hours ago                 pensive_cartwright
```

The first column `CONTAINER ID` allows you to chose and delete several containers at once
```bash
sudo docker rm b74e885e4a92 95078a9c5748
```

[Docker page 3](./Docker3.md)