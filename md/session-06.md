Packages are folders containing a `__init__.py` file.

Members with double underscores are referred to in Python as "dunder" names.  These can be viewed as magic, but they exist to convey a _behavior_ rather than concrete types.

This magic is usually represented in other languages as traits, interfaces, or protocols (in Python's case).

```sh
poetry new --src parse_args
cd parse_args
# poetry build
poetry install
New-Item -Path src/parse_args/__main__.py
```

```sh
python -m parse_args -arguments
```
