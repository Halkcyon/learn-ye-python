# Intro

Tools needed today:

- httpie
- pipx
- poetry

```sh
$ pip install --user pipx
...
$ py.exe -m pipx ensurepath --force
...
# at this point, close and re-launch your terminal
$ pipx install httpie
...
$ pipx install poetry
...
```

## FastAPI

FastAPI is a web framework for quickly building webapis.  It works by
registering functions and abstracting away the lower level infrastructure like
manually listening to sockets or parsing text into Python objects.  It
registers your functions by using a feature of Python called [_decorators_][1].
Decorators are plain Python functions that accept a function as an argument and
returns a different function, modifying the _behavior_ of the original
function.

[1]: <https://docs.python.org/3/glossary.html#term-decorator>
