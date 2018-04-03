# Dev system setup
```
# /etc/sysctl.conf
# Sharply reduce the inclination to swap
vm.swappiness=1

fs.inotify.max_user_watches = 524288
```
Then run this command to apply the change:
`sudo sysctl -p --system`