# Iqbal's Blog On The Internet

Notes so I remember what I needed to do to setup my personal blog site using
Pelican and GitHub Pages.

~~First, read [this](https://a-slide.github.io/blog/github-pelican) as a primer on how to use Pelican with GitHub Pages~~

# Preparation

These need to be done and installed first:

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install pelican markdown ghp-import pelican-i18n-subsites
```

```
$ make html
```

# Updating the blog

Just like a typical dev environment, when we want to write a new post, we can start with creating a branch. After
writing the post, you can do

```
make html
pelican -l -p 8080
```

which will create the static HTML files and run the dev server listening on 8080

Images go to `contents/images` while each directory represents a category

## Publishing to GitHub

The Tips page [here](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages) explains how to publish
to GitHub Pages. Since this blog uses `username.github.io`, [publishing to a user site](https://docs.getpelican.com/en/latest/tips.html#publishing-a-user-site-to-github-pages-from-a-branch) applies to us.

When you're ready to push the changes to GitHub Pages and publish, do:

```
$ git checkout main; make github
```

# Plugins

You'll need to checkout the plugins repo into the `plugin` directory:

```
$ cd plugins
$ git clone https://github.com/getpelican/pelican-plugins.git .
```

Included in this is the `i18n_subsites` which is needed for an internationalized blog.

# Themes

Live theme samples can be seen [here](https://pelicanthemes.com/).
Download the themes and plugin repo

```
$ git clone --recursive https://github.com/getpelican/pelican-themes themes
```

Not all themes can handle i18n, so we need to test and use only those that can.

# CNAME file

In order to use custom domains on GitHub Pages, you'll need to make sure the
CNAME file [gets published every time you do `make github`](https://stackoverflow.com/questions/33384328/how-can-i-add-a-cname-file-to-the-root-of-the-master)
