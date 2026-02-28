# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal blog website built with Pelican static site generator and published to GitHub Pages. The blog is multilingual (English, Japanese, Malay) using the i18n_subsites plugin.

**Published URL**: https://iqbalabdullah.net
**GitHub Pages Branch**: `master` (not `main`)

## Core Architecture

### Pelican Structure

- **Content**: Blog posts in `content/posts/YYYY/` organized by year, pages in `content/pages/`
- **Images**: Stored in `content/images/`
- **Output**: Generated static HTML in `output/` directory
- **Theme**: Currently uses `tuxlite_zf` from the `themes/` directory (entire pelican-themes repo is cloned)
- **Config Files**:
  - `pelicanconf.py`: Development configuration
  - `publishconf.py`: Production configuration (adds Matomo analytics, feeds)

### Multi-language Support

The blog uses the `i18n_subsites` plugin to support three languages:
- English (`en`) - default
- Japanese (`ja`)
- Malay (`ms`)

**Important**: Blog post filenames must end with language suffix (e.g., `-en.md`, `-ja.md`, `-ms.md`)

### URL Structure

Articles are saved with date-based paths:
```
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"
```

### CNAME File

The `CNAME` file is critical for custom domain support. It's stored in `content/extra/CNAME` and automatically copied to the output root via:
```python
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}
```

## Development Commands

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Building and Previewing

```bash
# Generate HTML (development settings)
make html

# Run development server with live reload on custom port
make devserver PORT=8080

# Alternative: Simple server with auto-regeneration
pelican -l -p 8080
```

### Publishing to GitHub Pages

```bash
# Build with production settings and push to master branch
make github
```

This command:
1. Runs `make publish` (builds with `publishconf.py`)
2. Uses `ghp-import` to commit output to `master` branch
3. Pushes to origin/master

**Critical**: GitHub Pages is configured to deploy from the `master` branch, not `main`.

## Python Tools

### edit.py - Blog Post Editor

Script for AI-assisted grammar correction and translation using local LLM (llama-cpp-python):

```bash
# Grammar correction
python edit.py input.md output.md [--gpu y]

# Translation to Japanese
python edit.py input.md output.md --translate ja [--gpu y]
```

**Requirements**:
- GGUF model file path in `.env` as `GGUF_FILE_PATH`
- Works with meta-llama-3-8b-instruct.Q3_K_M.gguf

**How it works**:
- Splits content on `<!-- EDPART -->` markers
- Uses prompts from `prompts.py` to fix grammar or translate
- Supports GPU acceleration via CUDA

### tasks.py - Invoke Tasks

Alternative to Makefile using Python's invoke library:

```bash
# Build site
invoke build

# Serve locally
invoke serve

# Live reload with browser auto-refresh
invoke livereload

# Publish to GitHub Pages
invoke gh_pages
```

### prompts.py

Contains system prompts and examples for the LLM editing/translation:
- `FIX_CONTENT_PROMPT`: Grammar and style corrections
- `TRANSLATE_CONTENT_TO_JA`: English to Japanese translation

## Publishing Workflow

From README.md, typical workflow for new posts:

1. Create a new branch (optional)
2. Write content in `content/posts/YYYY/post-name-{lang}.md`
3. Compress images (for performance)
4. Preview: `make devserver PORT=8080`
5. Merge to main (if on branch)
6. `git fetch`
7. `make github` - This builds and pushes to `master` branch

## Blog Post Format

Blog posts are Markdown files with metadata:

```markdown
Title: Post Title
Slug: post-slug
Lang: en
Date: 2025-06-27 07:30
Modified: 2025-06-27 07:30
Tags: tag1; tag2; tag3;
Status: published
Authors: Iqbal Abdullah
Summary: Brief summary of the post.

Post content here...

Images use: {static}/images/path/to/image.png
```

## Theme Customization

The themes directory contains the entire pelican-themes repository (forked at github.com/iqbalabd/pelican-themes). Not all themes support i18n - only use themes compatible with the i18n_subsites plugin.

### Theme CSS Files (`themes/tuxlite_zf/static/css/`)

- `normalize.css`: CSS reset
- `foundation.min.css`: Foundation framework (base styles)
- `style.css`: Custom theme overrides (loaded after Foundation)
- `pygments.css`: Syntax highlighting colors (loaded last)

### Syntax Highlighting

Code blocks use a **Monokai** color scheme (`pygments.css`) with dark background `#272822` and bright text colors for good contrast.

**Important**: Foundation CSS sets `code { color: #7f0a0c; font-weight: bold }` (dark red) which overrides Pygments colors on bare text inside `<code>` elements. This is counteracted by `.highlight pre code { color: #f8f8f2; font-weight: normal; }` in `style.css`. Do not remove this override or code blocks will become unreadable.

## External Dependencies

- **Pelican**: Static site generator
- **ghp-import**: For GitHub Pages deployment
- **pelican-i18n-subsites**: Multi-language support
- **llama-cpp-python**: For local LLM editing (optional)
- **fabric**: Alternative CLI tool for AI-assisted proofreading

## Key Differences from Standard Setup

1. GitHub Pages deploys from `master` branch (not `gh-pages`)
2. CNAME file management is automated via Pelican config
3. Multi-language support requires careful filename conventions
4. Local LLM tools for content editing (not typical for static blogs)
