- [Pandas](#pandas)
	- [Data Structures](#data-structures)
		- [Series](#series)
		- [DataFrames](#dataframes)
			- [Selection](#selection)
			- [Inserting values](#inserting-values)
			- [Deleting](#deleting)
			- [Nested Dictionaries](#nested-dictionaries)
		- [Index Objects](#index-objects)
	- [Essential Functionality](#essential-functionality)
		- [Reindexing](#reindexing)
		- [Indexing, Selection and Filtering](#indexing-selection-and-filtering)


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
> ```python
> val = pd.Series([-1.2, -1.5, -1.7], index=['a', 'd', 'f'])
> frame['non_existent_column'] = val
> frame
> #   state	year	pop		non_existent_column
> # id				
> # a	Ohio	2000	1.5		-1.2
> # b	Ohio	2001	1.7		NaN
> # c	Ohio	2002	3.6		NaN
> # d	Nevada	2001	2.4		-1.5
> # e	Nevada	2002	2.9		NaN
> # f	Nevada	2003	3.2		-1.7
> ```

#### Deleting
The `del` keyword can be used to delete columns: `del frame['non_existent_column']`.

For rows, you should use the `df.drop()` method with it's index: `frame.drop(index=['a', 'b'])`. The drop method also works for columns with `frame.drop(columns=['pop'])`.

> [!NOTE]
> You can also drop by specifying the axis parameter (as with NumPy): `frame.drop(list, axis=1)` with 1 for columns and 0 for rows.

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

### Index Objects

Pandas’s Index objects are responsible for holding the axis labels and other metadata. Any array or other sequence of labels you use when constructing a Series or DataFrame is internally converted to an Index. Index objects are immutable and thus can’t be modified by the user:
```python
obj = pd.Series(np.arange(3), index=["a", "b", "c"])

index = obj.index

index
Index(['a', 'b', 'c'], dtype='object')

index[1] = 'd' # TypeError
```

You can create and index object with `pd.Index(np.arange(5))`.

In addition to being array-like, an Index also behaves like a fixed-size set, although *it can* contain duplicate labels.

Check some [index methods here](https://wesmckinney.com/book/pandas-basics#tbl-table_index_methods).

## Essential Functionality
As the book says
> This book is not intended to serve as exhaustive documentation for the pandas library; instead, we'll focus on familiarizing you with heavily used features...

So, this is just a briefing of that, to come back to for review.

### Reindexing

`reindex` is a method in pandas objects, which creates a new object with the values rearranged to align with the new index.
```python
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
obj
# d    4.5
# b    7.2
# a   -5.3
# c    3.6
# dtype: float64

obj.reindex(["a", "b", "c", "d", "e"])
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    NaN
# dtype: float64
```

For ordered data, you can do interpolation or filling of values when reindexing. The method option is for that, using a method such as `ffill`, which forward-fills the values:
```python
obj = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
# 0      blue
# 2    purple
# 4    yellow
# dtype: object

obj.reindex(np.arange(6), method="ffill")
# 0      blue
# 1      blue
# 2    purple
# 3    purple
# 4    yellow
# 5    yellow
# dtype: object
```

With DataFrames, you can specify whether to reindex rows or columns (rows is the default). For that use the column parameter: `frame.reindex(columns=['column1','column2'])`. However, when reindexing by columns, if a column didn't exist, it will be created with all missing values and if a column, that does exist, is not included in the list, it will be dropped.

> [!NOTE]
> You can also just use the `reindex` function with the axis parameter: `frame.reindex(index_list, axis="columns")`.

[Here](https://wesmckinney.com/book/pandas-basics#tbl-table_reindex_function) are all the `reindex` function arguments.

### Indexing, Selection and Filtering