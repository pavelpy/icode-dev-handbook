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


## docker odoo
```
chown systemd-network:systemd-journal -R ./
chown 101:101 -R ./

```

## How to copy files from local machine to docker container on windows
Use docker cp.
`docker cp c:\path\to\local\file container_name:/path/to/target/dir/`
If you don't know what's the name of the container, you can find it using:
`docker ps --format "{{.Names}}"`


## postgres data
`PGDATA=/var/lib/postgresql/data/pgdata`

## copy postgres
`docker cp 9694bbb0b66d:/var/lib/postgresql/data /opt/odoo_instances/itwit_8039/backup/var_lib_postgresql_data`