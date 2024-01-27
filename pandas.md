# Pandas

An open source library for manipulating data with python. I'll be referring to pandas as `pd`.

Basic stuff here, check [full book](https://wesmckinney.com/book/) from pandas creator.

## Data Structures

The primary objects in pandas are the DataFrame, a tabular, column-oriented data structure with both row and column labels. And the Series, a one-dimensional labeled array object.

### Series
A Series is a one-dimensional array-like object containing a sequence of values of the same type and an associated array of data labels (index, not necessarily a number). If an index is not specified, a default one consisting of the integers 0 through N - 1 (where N is the length of the data) will be created. 

The string representation of a Series displayed interactively shows the index on the left and the values on the right:
```python
obj = pd.Series([4, 7, -5, 3])
obj
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64
```

You can get the array representation and index object of the Series via its array and index attributes, respectively:
```python
obj.array
# <PandasArray>
# [4, 7, -5, 3]
# Length: 4, dtype: int64

obj.index
# RangeIndex(start=0, stop=4, step=1)
```

To specify your own index use the `index` param:
```python
obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
obj2
# d    4
# b    7
# a   -5
# c    3
# dtype: int64

obj2.index
# Index(['d', 'b', 'a', 'c'], dtype='object')
```

Should you have data contained in a Python dictionary, you can create a Series from it by passing the dictionary as `pd.Series(dict)` (takes the keys as index). And you can convert it back to a dictionary with `dict_series.to_dict()`.

In case a key in your dict doesn't have a value (it's None), then pandas will take it as NaN and is considered in pandas to mark missing or NA values. The `isna` and `notna` functions in pandas should be used to detect missing data. This can be called with `pd.isna(series)` or as an instance method `series.isna()`.

Both the Series object itself and its index have a name attribute, which integrates with other areas of pandas functionality. You can set the name of the index with `series.index.name = 'name'` (like the column's name in DB's).

A Series’s index can be altered in place by assignment:
```python
obj
# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int64

obj.index = ["Bob", "Steve", "Jeff", "Ryan"]

obj
# Bob      4
# Steve    7
# Jeff    -5
# Ryan     3
# dtype: int64
```

### DataFrames

A DataFrame represents a rectangular table of data and contains an ordered, named collection of columns, each of which can be a different value type. The DataFrame has both a row and column index (can be though of like a dictionary of Series or as a DB table).

You can create a DataFrame from a dictionary of equal-length lists or NumPy arrays:
```python
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

frame
#     state  year  pop
# 0    Ohio  2000  1.5
# 1    Ohio  2001  1.7
# 2    Ohio  2002  3.6
# 3  Nevada  2001  2.4
# 4  Nevada  2002  2.9
# 5  Nevada  2003  3.2
```

Index defaults to integers, but you can change it as with Series (the name as well):
```python
frame.index = ['a','b','c','d','e','f']
frame.index.name = 'id'
frame
# 	state	year	pop
# id			
# a	Ohio	2000	1.5
# b	Ohio	2001	1.7
# c	Ohio	2002	3.6
# d	Nevada	2001	2.4
# e	Nevada	2002	2.9
# f	Nevada	2003	3.2
```

For large DataFrames, the `head` method selects only the first five rows, while `df.tail()` returns the last 5.

You can specify a sequence of columns and the DataFrame will be shown in that way. If you add a column that doesn't exist, the column will be created and all values will be set as missing:
```python
pd.DataFrame(data, columns=["year", "state", "pop", "non_existent_column"])

#    year   state  pop  non_existent_column
# 0  2000    Ohio  1.5                  NaN
# 1  2001    Ohio  1.7                  NaN
# 2  2002    Ohio  3.6                  NaN
# 3  2001  Nevada  2.4                  NaN
# 4  2002  Nevada  2.9                  NaN
# 5  2003  Nevada  3.2                  NaN
```
> [!WARNING]
> New columns cannot be created with the frame.new_column dot attribute notation.

#### Selection
A column in a DataFrame can be retrieved as a Series either by dictionary-like notation (`df['column']`) or by using the dot attribute notation (`df.column`). 

> [!NOTE]
> `df['column']` works for any column name while `df.column` works only when the column name is a valid Python variable name and does not conflict with any of the method names in DataFrame.

Rows can also be retrieved by position or name with the special iloc and loc attributes:
```python
frame.loc['a']
# state    Ohio
# year     2000
# pop       1.5
# Name: a, dtype: object

frame.iloc[1]
# state    Ohio
# year     2001
# pop       1.7
# Name: b, dtype: object
```

#### Inserting values
Columns can be modified by assignment. You can use:
* a scalar value: `frame['column'] = 5` and **all** rows in the dataframe will have that value in that particular column
* a list, array or Series: the value’s length must match the length of the DataFrame.

> [!IMPORTANT]
> If you assign a Series, its indexes will be realigned exactly to the DataFrame’s index, inserting missing values in any index values not present:

```python
val = pd.Series([-1.2, -1.5, -1.7], index=['a', 'd', 'f'])
frame['non_existent_column'] = val
frame
#   state	year	pop		non_existent_column
# id				
# a	Ohio	2000	1.5		-1.2
# b	Ohio	2001	1.7		NaN
# c	Ohio	2002	3.6		NaN
# d	Nevada	2001	2.4		-1.5
# e	Nevada	2002	2.9		NaN
# f	Nevada	2003	3.2		-1.7
```

#### Deleting
The `del` keyword can be used to delete columns: `del frame['non_existent_column']`.

For rows, you should use the `df.drop()` method with it's index: `frame.drop(index=['a', 'b'])`.

#### Nested Dictionaries
Another common form of data is a nested dictionary of dictionaries. If a nested dictionary used to construct a  DataFrame, pandas will interpret the outer dictionary keys as the columns, and the inner keys as the row indices (not true if you specify your own indexes):
```python
populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6}, "Nevada": {2001: 2.4, 2002: 2.9}}

frame2 = pd.DataFrame(populations)
frame2
# 		Ohio   Nevada
# 2000   1.5     NaN
# 2001   1.7     2.4
# 2002   3.6     2.9

# You can transpose it if you want
frame2.T
#  		   2000  2001  2002
# Ohio     1.5   1.7   3.6
# Nevada   NaN   2.4   2.9
```

> [!WARNING]
> Transposing discards the column data types if the columns do not all have the same data type, so transposing and then transposing back may lose the previous type information.

Besides dictionary of dictionaries you can have other data types in the DataFame constructor, check full list [here](https://wesmckinney.com/book/pandas-basics#tbl-table_dataframe_constructor)

Lastly, you can get a DataFrame information as a NumPy 2d array with `.to_numpy()` method.