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

or just

```
make devserver PORT=8080
```

which will create the static HTML files and run the dev server listening on 8080.
Images go to `contents/images` while each directory represents a category.

## Publishing to GitHub

- The Tips page [here](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages) explains how to publish
to GitHub Pages.
- Since this blog uses `username.github.io`, [publishing to a user site](https://docs.getpelican.com/en/latest/tips.html#publishing-a-user-site-to-github-pages-from-a-branch) applies to us.
- Set your GitHub Pages repo, as written [here](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).
- Remember to set the source to `Deploy from a branch` and the branch to `master` in your GitHub Pages settings, as
  written
  [here](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

### Publishing flow

This is a sample publishing flow for the blog

1. Checkout a new branch (optional)
1. Write your content
1. Compress your images to reduce load time
1. Proofread the content (optional)
1. `make devserver PORT=8080` and preview the post
1. Merge branch to main (if you did it on a new branch)
1. `git fetch`
1. `make github`

# Plugins

You'll need to checkout the plugins repo into the `plugin` directory:

```
$ cd plugins
$ git clone https://github.com/getpelican/pelican-plugins.git .
```

Included in this is the `i18n_subsites` which is needed for an internationalized blog.

# Themes

The Pelican themes repo is [here](https://github.com/getpelican/pelican-themes). Live theme samples can be seen [here](https://pelicanthemes.com/).

We can download the themes as it is like
```
$ git clone --recursive https://github.com/getpelican/pelican-themes themes
```

But since we most probably want to make changes to the theme, we should use our own fork:
```
$ git clone git@github.com:iqbalabd/pelican-themes.git themes
```

Not all themes can handle i18n, so we need to test and use only those that can.

# CNAME file

In order to use custom domains on GitHub Pages, you'll need to make sure the
CNAME file [gets published every time you do `make github`](https://stackoverflow.com/questions/33384328/how-can-i-add-a-cname-file-to-the-root-of-the-master)

# おまけ

## proofread with Llama

Build llama-cpp-python with CUDA to enable GPU usage
```
CMAKE_ARGS="-DLLAMA_CUDA=on" pip install --upgrade --force-reinstall --no-cache-dir llama-cpp-python
```

[`meta-llama-3-8b-instruct.Q3_K_M.gguf`](https://huggingface.co/SanctumAI/Meta-Llama-3-8B-Instruct-GGUF/blob/main/meta-llama-3-8b-instruct.Q3_K_M.gguf) works best
Tried [`mistral-7b-instruct-v0.2.BF16.gguf`](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.BF16.gguf) the model was loaded but it didn't follow instructions.
