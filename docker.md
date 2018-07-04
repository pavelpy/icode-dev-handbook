# Docker
## How to get bash or ssh into a running container in background mode?
```
$ sudo docker attach 665b4a1e17b6 #by ID
or 
$ sudo docker attach loving_heisenberg #by Name
$ root@665b4a1e17b6:/# 
```
if we want open new terminal with new instance of container's shell, we just need run the following:
```
$ sudo docker exec -i -t 665b4a1e17b6 /bin/bash #by ID
or
$ sudo docker exec -i -t loving_heisenberg /bin/bash #by Name
$ sudo docker exec -it --user root test bash
$ root@665b4a1e17b6:/#
```
