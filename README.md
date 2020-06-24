# The Fortunate

Notes so I remember what I needed to do to setup my personal blog site using
Pelican and GitHub Pages.

First, read [this](https://a-slide.github.io/blog/github-pelican) as a primer on how to use Pelican with GitHub Pages

# Basic branches

## main

This is where we write the contents and test them on localhost first:

```
$ make html && make serve
```

To make the flow easy to understand and simliar to a typical development flow,
we can create branches for drafts of different posts, but branches should be merged to back to `main` before being
published online. Treat `main` as the `master`.

Images go to `contents/images` while each directory represents a category

When you're ready to push the changes to GitHub Pages and publish, do:

```
$ git checkout main
$ make github
```

### CNAME file

In order to use custom domains on GitHub Pages, you'll need to make sure the
CNAME file gets published everytime you do `make github`:

https://stackoverflow.com/questions/33384328/how-can-i-add-a-cname-file-to-the-root-of-the-master

## master

The `master` branch is not used directly, but is only used by GitHub Pages to
publish the html files.
