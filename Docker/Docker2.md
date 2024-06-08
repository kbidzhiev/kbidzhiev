# Using your first container "The Swiss Army knife of Embedded Linux" - [BusyBox](https://en.wikipedia.org/wiki/BusyBox)

To get started do the following
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