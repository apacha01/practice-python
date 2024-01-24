# Python
A dynamic, interpreted (bytecode-compiled) language. 

Some basic concepts:
* There are no types (there are type hints, but python doesn't use them, it's just for the IDE's and a better dev experience).
* Each line is a statement (the line break is like semicolon in C).
* Uses indentation for block level grouping (instead of having brackets `{}`).
* File extension is `.py`.

## Python code

### Modules
Every file is a module (like in JS) and you can import them with the `import something from module` expression. When a Python file is run directly, the special variable "__name__" is set to "__main__", so it's common to have something the following in your source code:
```python
if __name__ == '__main__':
    main()
```

### User defined functions
To create a function use the `def` keyword followed by the name, then the parameters in between parenthesis and end with a colon (`:`).
```python
def greet(name):
	print('Hello there', name)
```

### Command Line
You run python files with the `python3` command. If you need to pass parameters then use the `sys` module's `argv` property with `argv[0]` being the program itself, `sys.argv[1]` the first argument, and so on.
```python
# hello.py
import sys

def main():
    print('Hello there', sys.argv[1]) # sys.argv[0] = 'hello.py'
```
And you run this with: `python3 hello.py Bob`.

### Variables
Python is case sensitive, so `a` and `A` are two different variables.

You don't need a type so just doing `x = 1` will create the `x` variable and set it's value to `1`. You can then reassign a value to it or just delete it (free up the memory) with `del x`.

### Code checking
Python does very little checking at compile time, deferring almost all type, name, etc. checks on each line until that line runs (runtime).
```python
def main():
    if name == 'Guido':
        print(greeeeeeet(name) + '!!!') # Pay special attention to this line!!!
    else:
        print(greet(name))
```
You'll see that the function `greet` defined in [this section](#user-defined-functions) is misspelled as `greeeeeeet`. However, the above code will compile and run perfectly until `name` is `'Guido'` and it actually goes in the `if` statement where it will give an error.
