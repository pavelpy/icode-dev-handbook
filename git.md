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

## work with some folders
```
git init <repo>
cd <repo>
git remote add -f origin <url>
git config core.sparseCheckout true
echo "some/dir/" >> .git/info/sparse-checkout
echo "another/sub/tree" >> .git/info/sparse-checkout
```
[source](https://stackoverflow.com/questions/600079/is-there-any-way-to-clone-a-git-repositorys-sub-directory-only)
[source](http://jasonkarns.com/blog/subdirectory-checkouts-with-git-sparse-checkout/)
