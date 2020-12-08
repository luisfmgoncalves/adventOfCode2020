Python is a dynamic, interpreted (bytecode-compiled) language. There are no type declarations of variables, parameters,
 functions or methods in source code. Python tracks the types of all values at runtime and flags code that
 does not make sense as it runs.

## Introduction

#### Run

Run a module:
`$python test.py`

Rund a module passing commando line argument:
`$python test.py hello`

#### Imports, Command-line arguments and `len()`

A Python module can be run directly — "python hello.py Test" — or it can be imported and used by some other module.
 When a Python file is run directly, the special variable `__name__` is set to `__main__`. 
 Therefore, it's common to have the boilerplate `if __name__ ==...` to call a main() function when the module
 is run directly, but not when the module is imported by some other module.
 
In a standard Python program, the list sys.argv contains the command-line arguments in the standard way with sys.argv[0]
 being the program itself, sys.argv[1] the first argument, and so on. If you know about argc, or the number of arguments,
 you can simply request this value from Python with len(sys.argv).
In general, len() can tell you how long a string is, the number of elements in lists and tuples (another array-like data structure),
 and the number of key-value pairs in a dictionary.
 
#### User defined functions

```
def repeat(s, exclaim):
    """
    This is a comment
    """

    result = s * 3
    if exclaim:
        result = result + '!!!'
    return result
```

Both `+` and `*` are called "overloaded" operators because they mean different things for numbers vs. for strings.

#### Indentation
Whitespace indentation of a piece of code affects its meaning.
A logical block of statements such as the ones that make up a function should all have the same indentation,
 set in from the indentation of their parent function or "if" or whatever. If one of the lines in a group has a different
 indentation, it is flagged as a syntax error.

How many spaces should I indent?
According to the official Python style guide (PEP 8), you should indent with 4 spaces. But 2 is fine.

#### Modules and namespaces
A function has a fully qualified name of `test.foo` if is defined as `def foo()` in the module `test.py`.

```
  import sys

  sys.exit(0)
```
With the statement "import sys" you can then access the definitions in the sys module and make them available by their
 fully-qualified name, e.g. sys.exit().
Standard libraries:

`sys` — access to exit(), argv, stdin, stdout, ...

`re` — regular expressions

`os` — operating system interface, file system

More standard libraries [here](https://docs.python.org/3/library/) 

#### `help()` and `dir()`

Inside the Python interpreter, the help() function pulls up documentation strings for various modules, functions, and methods.
These doc strings are similar to Java's javadoc. The dir() function tells you what the attributes of an object are.
