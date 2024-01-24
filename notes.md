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

You can declare variables individually
```python
x = 1
y = 2.5
name = 'John'
is_true = True
```
Or use a destructuring like syntax (as in JS) and assign all values in one line, the following code is equivalent to the one above:
```python
x, y, name, is_true = (1, 2.5, 'John', True)
```
> [!IMPORTANT]
> Python has some built-in functions, like len(data) which returns the length of the data structure that you passed as parameter. A common error is to use the `len` word as a variable and store something in there, don't. There are reserved words like `while` and `if` that throw errors, but built-in functions/variables don't act like that, so you would just be overwriting whatever values were there.


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


## Strings
* Python has a built in class named `str`.
* Python strings are "immutable" (can't be changed after created).
* Strings be in single or double quotation marks.
* Usual concatenation methods like using the `+` operator works, but python also allows things like `'-'*10` which will display the `-` character ten times.
* You can find some string methods on [python docs](https://docs.python.org/3/library/stdtypes.html#string-methods).
* Unlike in other languages, the `==` is optimized to compare strings in Python.

### Formatting

#### .format() method
You can pass arguments as needed to the `.format()` function and every value in between brackets (`{}`) will be replaced:
```python
print('Hello {name}, are you really {age} years ol? Quite {just_a_variable}'.format(name='John', age=105, just_a_variable='old'))
# Or if the values are already in variables
print('Hello {name}, are you really {age} years ol? Quite {just_a_variable}'.format(name=name, age=age, just_a_variable=some_variable))
```

#### f strings - since python 3.6
You can do the exact same thing as with the `.format()` but without having to pass the values separately if you prepend an `f` to the string:
```python
print(f'Hello {name}, are you really {age} years ol? Quite {just_a_variable}')

# with objects
car = {'tires':4, 'doors':2}
print(f'car = {car}') # car = {'tires': 4, 'doors': 2}
```
#### % operator
The % operator takes a printf-type (from `C`) format string on the left, and the matching values in a tuple on the right.
```python
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
```

### Slices
The *slice* syntax is a way to refer to sub-parts of sequences. The slice `s[start:end]` is the elements beginning at start and extending up to but not including end.

You can access a string using the standard `[]` syntax with indexes (zero-based). Also, python uses negative numbers to give easy access to the chars at the end of the string: s[-1] is the last char.

![Python List with indexes explained](image.png)

**Positive indexes:**

* `s[1:4]` is `'ell'`: chars starting at index 1 and extending up to but not including index 4
* `s[1:]` is `'ello'`: omitting either index defaults to the start or end of the string
* `s[:]` is `'Hello'`: omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence)
* `s[1:100]` is `'ello'`: an index that is too big is truncated down to the string length

**Negative indexes:**

* `s[-1]` is `'o'`: last char (1st from the end)
* `s[-4]` is `'e'`: 4th from the end
* `s[:-3]` is `'He'`: going up to but not including the last 3 chars.
* `s[-3:]` is `'llo'`: starting with the 3rd char from the end and extending to the end of the string.

### Byte vs Unicode
Regular strings are unicode, but Python also supports strings composed of plain bytes (denoted by the prefix `b` in front of a string literal) like:
`byte_string = b'A byte string'`.
```python
ustring = 'A unicode \u018e string \xf1'
b = ustring.encode('utf-8')
print(b) # outputs -> b'A unicode \xc6\x8e string \xc3\xb1' 				
t = b.decode('utf-8')
print(t == ustring) # True
```