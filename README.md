# The Fortunate

Notes so I remember what I needed to do to setup my personal blog site using
Pelican and GitHub Pages.

First, read [this](https://a-slide.github.io/blog/github-pelican) as a primer on how to use Pelican with GitHub Pages

# Basic branches

## source

This is where we write the contents and test them on localhost first:

```
$ make html && make serve
```

Images go to `contents/images` while each directory represents a category

When you're ready to push the changes to GitHub Pages and publish, do:

```
$ make github
```

### CNAME file

In order to use custom domains on GitHub Pages, you'll need to make sure the
CNAME file gets published everytime you do `make github`:

https://stackoverflow.com/questions/33384328/how-can-i-add-a-cname-file-to-the-root-of-the-master

## master

The `master` branch is not used directly, but is only used by GitHub Pages to
publish the html files.
