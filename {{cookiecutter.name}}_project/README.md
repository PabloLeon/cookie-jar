# {{cookiecutter.name}}

{{cookiecutter.description}}

# Installation

Requires anaconda as virtual environment. Run `conda env create -f environment.yml` to create the environment. This installs all code from `{{cookiecutter.name}}` and allows us to import it as if it was a package! After installing the dependencies, activate with `conda activate {{cookiecutter.name}}`.

# Directory structure

Inspired by this gist: https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510

```
    |- notebooks/
    |- 01-first-logical-notebook.ipynb
    |- prototype-notebook.ipynb
    |- archive/
        |- no-longer-useful.ipynb
    |- projectname/
    |- projectname/
        |- __init__.py
        |- config.py
        |- data.py
        |- utils.py
    |- setup.py
    |- README.md
    |- data/
    |- raw/
    |- processed/
    |- cleaned/
    |- scripts/
    |- script1.py
    |- script2.py
    |- archive/
        |- no-longer-useful.py
    |- environment.yml
```

# Datasets
