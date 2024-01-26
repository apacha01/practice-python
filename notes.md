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

#### Lambda Functions
Like arrow functions in JS. Small one time use anonymous functions:
```python
lambda param1, param2: param1 + param2
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


## Data Structures

### Slices
Slices are objects usually containing a part of a sequence that's created with the `[]` notation. Works for any sequence just like in strings.

E.g. for a list `l = [1,2,3,4,5]`:
* `l[:]` returns `[1,2,3,4,5]`
* `l[1:]` returns `[2,3,4,5]`
* `l[2:4]` returns `[3,4]`
* `l[-1]` returns `5`

### Lists
A list is a sequence:
* Zero-based indexed
* Ordered (items are in the list in the order they are inserted, doesn't mean sorted)
* Changeable or Mutable
* It allows duplicate items

From python docs:
>  it is more akin to an array in other languages than to a linked list since access to elements is O(1).

You can create a list like:
* `[]`: `l = [1,2,3,4,5]`
* `list()`: `l2 = list((1,2,3,4,5))`
* List comprehension: `l3 = [n * n for n in some_iterable]`

Python docs on list comprehension:
> A compact way to process all or part of the elements in a sequence and return a list with the results.

Assignment with an `=` on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.

The `+` works to append two lists, so `[1, 2] + [3, 4]` yields `[1, 2, 3, 4]`. This is a new list, regardless whether the second expression is empty or not so:
```python
>>> l = [1,4,8,2,9]
>>> l2 = l
>>> l.append(1)
>>> l
[1,4,8,2,9,1]
>>> l2
[1,4,8,2,9,1]
>>> l3 = l2 + []
>>> l2.append(99)
>>> l
[1,4,8,2,9,1,99]
>>> l2
[1,4,8,2,9,1,99]
>>> l3
[1,4,8,2,9,1]
```

### Tuples
A tuple is a sequence:
* Zero-based indexed
* Ordered (items are in the tuple in the order they are inserted, doesn't mean sorted)
* Immutable
* It allows duplicate items

You can create a tuple like:
* Separating items with comma: `t = 1,2,3,4,5`
* `()`: `t2 = (1,2,3,4,5)`
* `tuple()`: `t3 = tuple((1,2,3,4,5))`

> [!NOTE]
> If you want to make a one item tuple the use a trailing coma, otherwise python will just take it as an expression in between parenthesis:
> `t = (1,)`
> If there is syntactic ambiguity, then the parenthesis cannot be omitted. E.g. a function `hi(names: tuple[str])` calling `hi('John','Mary','Some Name')` is interpreted as multiple parameters instead of a tuple, in which case parenthesis should be used.

### Sets
A set is a collection:
* There is no index
* Unordered (items are not in the set in the order they are inserted)
* Mutable
* It doesn't allows duplicate items

You can create a set like:
* `{}`: `s = {1,2,3,4}`
* `set()`: `s2 = set((1,2,3,4,5))`
* Set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`

> [!NOTE]
> For empty sets `{}` doesn't work (it creates an empty [dict](#dicts)) so use `set()`.

### Dicts
A dictionary is a collection with `key:value` pairs:
* Indexed by keys (so strings, not integers)
* Unordered (items are not in the dict in the order they are inserted)
* Mutable
* It doesn't allows duplicate items

You can create a dict like:
* `{}`: `ages = {'john': 45, 'doe': 20}`

You access an item with the `[]` syntax: `ages['john]`. If you want the keys/values only, use the `.keys()` or `.items()` respectively (returns a list).

> [!NOTE]
> `dict[non_existent_key]` throws an error. If you want to avoid that use the `dict.key(non_existent_key)` which returns None if value is not present.

#### String % operator with dicts
The % operator works conveniently to substitute values from a dict into a string by name:
```python
h = { count: 42, word: 'garfield' }
s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
# 'I want 42 copies of garfield'
```

### Del
`del` is a keyword for deleting variables or values in some data structure.

Referring to a variable that was deleted with `del` will throw an error. It is as if the variable was never created.

Some examples on how to use it:
* `del dict['key']` which deletes that specific key.
* `del dict` which deletes the entire dictionary.
* `del list[2:]` which deletes the all elements from index 2 to the end.


## The range() function
The `range(n)` function yields the numbers `0, 1, ... n-1`, and `range(a, b)` returns `a, a+1, ... b-1` up to but not including the last number.

This sequence returned is not a list, but of type `range`.

## Operators
Only python specific ones will be here, check [the docs](https://docs.python.org/3/reference/lexical_analysis.html#operators) to see all operators.

### Logical operators:
* `and`: like `&&` in C
* `or`: like `||` in C
* `not`: like `~` in C

### Membership operators:
* `in`: checks whether a value is in a collection. E.g. `1 in [1,2,3,4]` which returns `True`

### Identity operators
* `is`: checks whether the identity is the same, when the variables on either side points at the exact same object returns true. (so pointer comparison more than value comparison).

Check this example:
```python
>>> string1 = 'hello'
>>> string2 = 'hello'
>>> id(string1)
139699879691376
>>> id(string2)
139699879691376
>>> string1 == string2
True
>>> string1 is string2
True
>>> string1 = string1.replace('h', 'm')
>>> string1 = string1.replace('m', 'h')
>>> string1
'hello'
>>> string2
'hello'
>>> string1 == string2
True
>>> string1 is string2
False
>>> id(string1)
139699879691568
>>> id(string2)
139699879691376
```

## Files
Open a file with the `open(filename)` function. This function returns a file handler to which you should call `handler.close()` after you finished using it.

You can use the `with` keyword to avoid closing a file.
```python
with open(filename, mode) as f: # mode = {'r' | 'w' | 'a' | 'rt'}
	# do file stuff here...
	for line in f:
		# do something with each line. Only works for text files, no binary files
```

The `open()` functions as some options like the `mode` in which it is opened. You can read ('r'), write ('w'), append ('a') or you can read and write ('r+').

## Classes
The concept is the same as in every other language. You declare a class with the `class` keyword.

Constructor is defined as `__init__` function. This function takes in a param `self` (obviously name it however you want) that is the object itself. Use that `self` value to refer to an instance specific property (like `this` in JS).

This types of functions are called dunder functions (double underscore).

Example:
```python
class User:
	def __init__(self, param1, param2):
		self.name = param1
		self.lastName = param2
	
	# Just a method
	def greet(self):
		print(f'Hello {self.name}')

# Instance an object of that class
u = User('John', 'Doe')
print(u.name) # 'John'
print(u.greet()) # Hello John
```

### Inheritance
There is no keyword for this, you `call` your class with the parent class as a parameter.

Example:
```python
class Admin(User):
	def greet(self):
		print('I am and admin and this overwrites the greet method in user!')

a = Admin('admin', 'last name')
print(a.name) # 'admin'
a.greet() # 'I am and admin and this overwrites the greet method in user!'
```

# NumPy

Short for Numerical Python, a library for Python.

I'll be referencing numpy with `np`.

## Arrays
NumPy has their own array called `ndarray`, which is not a class (so you can't check for instances of that with `isinstance(x,np.array)`, it gives a `TypeError`)

* Create an array with `arr = np.array(<data>)`. You could specify the data type with an additional param called `dtype`, e.g. default for integers is `int32` (check all data types [here](https://wesmckinney.com/book/numpy-basics#tbl-table_array_dtypes)).
* Create empty array with `np.empty((2,2))` with the tuple passed being the dimensions (doesn't have to be 2d). This doesn't even initialized the values so you'll get garbage. You can use `np.zeros((2,2))` to do the same but initialize all values to 0, or `np.ones()` to initialize all values with ones.
* Create array following a sequence with `np.arrange(n[, m, steps])` with `n` being the data that goes from 0 to n-1 or from `n` to `m` if `m` is specified. `steps` is just the amount `n` is increased by in each iteration until it gets to `m`.
* Create an array with `n` items with `np.linspace(n, m, items)`. This creates an array with `items` items in between `n` and `m`.
* Check dimensions with `arr.shape # (2,2)` (gives columns size first).
* Check total amount of data with `arr.size # 4 (following dimensions example)`.

### Arithmetic Operations
Any arithmetic operations between equal-size arrays apply the operation element-wise:
```python
arr = np.array([[1., 2., 3.], [4., 5., 6.]])

arr * arr
# array([[ 1.,  4.,  9.],
#        [16., 25., 36.]])

arr - arr
# array([[0., 0., 0.],
#        [0., 0., 0.]])
```

Arithmetic operations with scalars propagate the scalar argument to each element in the array:
```python
1 / arr
# array([[1.    , 0.5   , 0.3333],
#        [0.25  , 0.2   , 0.1667]])
```

Comparisons between arrays of the same size yield Boolean arrays:
```python
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

arr2 > arr
# array([[False,  True, False],
#        [ True, False,  True]])
```

### Some methods
From all `ndarrays`, you have:
* `arr.min()` for minimum
* `arr.max()` for maximum
* `arr.mean()` for the median
* `arr.std()` for the standard deviation
* `arr.sum()` adds up all values in the array

and such

When working with 2d arrays (matrices) things like min function or max will work across the columns or files depending on the axis specified:
```python
import numpy as np

arr = np.array([
	[6,  8,  11,  8]
	[13, 14,  0,  0],
	[5,  10,  1,  2],
	[18, 16, 14,  2],
])

arr.min(axis = 0) # columns, takes the min of every column
# [5, 8, 0, 0]

arr.max(axis = 1) # rows, takes the min of every row
# [11, 14, 10, 18]
```

### Selection

The slices and indexing that applies to python sequences and strings is used here, so use `[]`.

#### Basic Indexing

For 2d arrays you use the basic `[]` syntax. You can use `arr[0][2]` or `arr[0,2]` to select the third column in the first row:
```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d[0][2]
# 3

arr2d[0, 2]
# 3
```

In multidimensional arrays, if you omit later indices, the returned object will be a lower dimensional ndarray consisting of all the data along the higher dimensions.
```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d[0]
# [1, 2, 3]
```

You can select a set of values of a `ndarray` with the booleans arrays seen in the [arithmetic operations section](#arithmetic-operations) of the arrays:
```python
arr>12 # returns the boolean matrix
# [
# 	[False,  False,  False,  False],
# 	[True,    True,  False,  False],
# 	[False,  False,  False,  False],
# 	[True,    True,  True,   False]
# ]

arr[arr>12] # You do lose the shape
# [13, 14, 18, 16, 14]
```

> [!IMPORTANT]
> The Python keywords `and` and `or` do not work with Boolean arrays. Use `&` (and) and `|` (or) instead.

#### Fancy Indexing

To select a subset of the rows in a particular order, you can simply pass a list or ndarray of integers specifying the desired order:
```python
arr = np.array([[0., 0., 0., 0.],
       [1., 1., 1., 1.],
       [2., 2., 2., 2.],
       [3., 3., 3., 3.],
       [4., 4., 4., 4.],
       [5., 5., 5., 5.],
       [6., 6., 6., 6.],
       [7., 7., 7., 7.]])

arr[[4, 3, 0, 6]]
# array([[4., 4., 4., 4.],
#        [3., 3., 3., 3.],
#        [0., 0., 0., 0.],
#        [6., 6., 6., 6.]])

# Using negative indices selects rows from the end:
arr[[-3, -5, -7]]
# array([[5., 5., 5., 5.],
#        [3., 3., 3., 3.],
#        [1., 1., 1., 1.]])

```

Passing multiple index arrays selects a one-dimensional array of elements corresponding to each tuple of indices:
```python
arr = np.array([
	[ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11],
    [12, 13, 14, 15],
    [16, 17, 18, 19],
    [20, 21, 22, 23],
    [24, 25, 26, 27],
    [28, 29, 30, 31]]
)

arr[[1, 5, 7, 2], [0, 3, 1, 2]] # so, tuple (1,0) -> arr[1,0] -> 4
# array([ 4, 23, 29, 10])
```

## Math functions

You have the typical trigonometric functions:
* `np.sin()`
* `np.cos()`
...

There's also a submodule for linear algebra which is `linalg` and you can use it like this:
```python
import numpy as np

A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))
# Matrix A raised to power 3:
#  [[336 162 228]
#  [406 162 469]
#  [698 702 905]]
```
## Randomness
A way to produce random numbers is using `np.random.default_rng(seed)` which you can pass a `seed` to and returns an object to which you can ask random numbers (`seed` is important for reproducibility).
```python
rg = np.random.default_rng(17)

print(rg.random(1)) # 1 is the amount of random numbers to get
# array([0.29924217]) - i made this up
```

If you only want integers the use `rg.integers(n [, m][, size])` with `n` being the data that goes from 0 to n-1 or from `n` to `m` if `m` is specified. `size` is the amount of items you'll get, always in between 0 and n-1 or `n` and `m`.

You can have a normal data as well with `rg.normal(media, std_deviation, n)` with `n` being the amount of data wanted (also follows the `seed` passed when creating rg).


# Pandas

Basic stuff here, check [full book](https://wesmckinney.com/book/) from pandas creator.

## Data Structures

The primary objects in pandas are the DataFrame, a tabular, column-oriented data structure with both row and column labels. And the Series, a one-dimensional labeled array object.