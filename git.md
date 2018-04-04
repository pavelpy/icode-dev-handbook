# Git
## Useful git alias
```
alias.co checkout
alias.ci commit
alias.st status
alias.br branch
alias.hist log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
alias.type cat-file -t
alias.dump cat-file -p
```

## clone branch
`git clone -b my-branch https://git@github.com/username/myproject.git`
`git clone -b opencv-2.4 --single-branch https://github.com/Itseez/opencv.git`