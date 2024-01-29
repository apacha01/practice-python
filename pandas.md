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
			- [Series](#series-1)
			- [DataFrames](#dataframes-1)
		- [Arithmetic and Data Alignment](#arithmetic-and-data-alignment)
			- [Filling values](#filling-values)
			- [Operations Between DataFrames and Series](#operations-between-dataframes-and-series)
		- [Function Application](#function-application)
		- [Sorting and Ranking](#sorting-and-ranking)
			- [Sorting](#sorting)
			- [Ranking](#ranking)
		- [Axis Indexes with Duplicate Labels](#axis-indexes-with-duplicate-labels)
	- [Computing Descriptive Statistics](#computing-descriptive-statistics)
		- [Correlation and Covariance](#correlation-and-covariance)
		- [Unique Values, Value Counts, and Membership](#unique-values-value-counts-and-membership)
	- [Data Loading, Storage, and File Formats](#data-loading-storage-and-file-formats)
		- [Reading and Writing Data in Text Format](#reading-and-writing-data-in-text-format)
			- [Basic CSV reading](#basic-csv-reading)
				- [Reading text files in pieces](#reading-text-files-in-pieces)
				- [Writing data to text format](#writing-data-to-text-format)
				- [Working with Other Delimited Formats](#working-with-other-delimited-formats)
			- [JSON Data](#json-data)
			- [XML and HTML](#xml-and-html)
				- [Parsing HTML](#parsing-html)
				- [Parsing XML](#parsing-xml)


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
> New columns cannot be created with the `frame.new_column` dot attribute notation.

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

You can also modify the name of the column with `frame.rename('old_column': 'new_column')`, or the type of the column with `frame['column'].astype(<type>)`.

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

#### Series
While you can select data by label with the `[]` syntax, the preferred way to select index values is with the special `loc` operator: `frame.loc[['col1','col2']]`. The reason to prefer loc is because of the different treatment of integers when indexing with `[]`. Regular `[]`-based indexing will treat integers as labels if the index contains integers. E.g:
```python
obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])
obj2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

obj1
# 2    1
# 0    2
# 1    3
# dtype: int64

obj2
# a    1
# b    2
# c    3
# dtype: int64

obj1[[0,1]] # index lookup
# 0    2
# 1    3
# dtype: int64

obj2[[0,1]] # rows order lookup
# a    1
# b    2
# dtype: int64

obj1[-1] # Throws error (pandas doesn't know whether to do label-based indexing or position-based)
```

Something like `loc[[0,1]]` fails if the index is not of the data passed to it (integer in this case). Since loc operator indexes exclusively with labels, there is also an `iloc` operator that indexes exclusively with integers to work consistently whether or not the index contains integers.

There's also slicing with `loc` by doing `obj2.loc["b":"c"]`.

> [!IMPORTANT]
> If you use `loc` to slice do note that it's not the same as Python, because `loc` does include the endpoint. Following the previous example, this would be the result:
> ```python
> obj2.loc["b":"c"]
> # b    2
> # c    3
> # dtype: int64
> ```

To filter a Series object you can use the Boolean array method seen in [this section](./numpy.md#basic-indexing):
```python
obj1[obj1>2]
# 1    3
# dtype: int64
```

#### DataFrames

Indexing into a DataFrame with `[]` retrieves one or more columns either with a single value or sequence. Indexing like this has a few special cases, like slicing or selecting data with a Boolean array (as seen in the [Basic Indexing](./numpy.md#basic-indexing) section in `numpy.md`).
```python
# data =
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

data["two"]
# Ohio         1
# Colorado     5
# Utah         9
# New York    13
# Name: two, dtype: int64

# Special case: Slicing to select rows
data[:2]
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7

# Special case: Boolean Arrays
data[data["three"] > 5]
# 		   one  two  three  four
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15
```

You can also use `loc` and `iloc` as with Series. Since DataFrame is two-dimensional, you can select a subset of the rows and columns with NumPy-like notation using either axis labels (loc) or integers (iloc).
```python
# loc
data.loc["Colorado"]
# one      4
# two      5
# three    6
# four     7
# Name: Colorado, dtype: int32

data.loc[['Colorado', 'New York']]
# 			one	two	three	four
# Colorado	4	5	6		7
# New York	12	13	14		15

data.loc["Colorado", ["two", "three"]]
# two      5
# three    6
# Name: Colorado, dtype: int32

# iloc
data.iloc[2]
# one       8
# two       9
# three    10
# four     11
# Name: Utah, dtype: int32

data.iloc[-1]
# one      12
# two      13
# three    14
# four     15
# Name: New York, dtype: int32

data.iloc[2, [3, 0, 1]]
# four    11
# one      8
# two      9
# Name: Utah, dtype: int32
```

Both methods work with slices as well:
```python
data.loc[:"Utah", "two"]
# Ohio        1
# Colorado    5
# Utah        9
# Name: two, dtype: int32

data.iloc[:, :3]
# 			one	two	three
# Ohio		0	1	2
# Colorado	4	5	6
# Utah		8	9	10
# New York	12	13	14
```
> [!NOTE]
> Boolean arrays can be used with `loc` but not `iloc`.

[Here is a list](https://wesmckinney.com/book/pandas-basics#tbl-table_dataframe_loc_iloc) of the indexing options in a DataFrame from McKinney book.

You can filter with the `loc` method and Boolean Arrays:
```python
data.loc[data["four"] > 5]
# 			one	two	three	four
# Colorado	4	5	6		7
# Utah		8	9	10		11
# New York	12	13	14		15
```

### Arithmetic and Data Alignment

pandas makes it simpler to work with objects with different indexes. E.g, when adding objects, if any index pairs are not the same, the respective index in the result will be the union of the index pairs:
```python
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4], index=["a", "c", "e", "f"])
# s1							s2
# a    7.3						a   -2.1
# c   -2.5						c    3.6
# d    3.4						e   -1.5
# e    1.5						f    4.0
# dtype: float64				dtype: float64

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"), index=["Ohio", "Texas", "Colorado"])
df2 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bde"), index=["Utah", "Ohio", "Texas"])
# df1								df2
# 			b    c    d						b     d     e
# Ohio      0.0  1.0  2.0			Utah    0.0   1.0   2.0
# Texas     3.0  4.0  5.0			Ohio    3.0   4.0   5.0
# Colorado  6.0  7.0  8.0			Texas   6.0   7.0   8.0

s1 + s2
# a    5.2
# c    1.1
# d    NaN
# e    0.0
# f    NaN
# dtype: float64

df1 + df2
# 			b   c     d   e
# Colorado  NaN NaN   NaN NaN
# Ohio      3.0 NaN   6.0 NaN
# Oregon    NaN NaN   NaN NaN
# Texas     9.0 NaN  12.0 NaN
# Utah      NaN NaN   NaN NaN
```

If you add objects with no column or row labels in common, the result will contain all nulls (NaN).

#### Filling values

If instead of using the `+` you use the `.add()` method you can chose a `fill_value` for any missing value:
```python
df1 + df2
# 			b   c     d   e
# Colorado  NaN NaN   NaN NaN
# Ohio      3.0 NaN   6.0 NaN
# Oregon    NaN NaN   NaN NaN
# Texas     9.0 NaN  12.0 NaN
# Utah      NaN NaN   NaN NaN

df1.add(df2, fill_value=0)
# 			b		c		d		e
# Colorado	6.0		7.0		8.0		NaN
# Ohio		3.0		1.0		6.0		5.0
# Texas		9.0		4.0		12.0	8.0
# Utah		0.0		NaN		1.0		2.0
```

Note that it doesn't prevent missing values if there is a column missing in both tables that's added.

The examples given where just on addition, you can find a detailed list of all operations with it's respective function [here](https://wesmckinney.com/book/pandas-basics#tbl-table_flex_arith).

#### Operations Between DataFrames and Series

As with [NumPy arrays of different dimensions using broadcasting](./numpy.md#broadcasting), arithmetic between DataFrame and Series is also defined, and they are similar. Consider the following data:
```python
frame
#           b     d     e
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0

series = frame.iloc[0]
# b    0.0
# d    1.0
# e    2.0
# Name: Utah, dtype: float64
```

By default, arithmetic between DataFrame and Series matches the index of the Series on the columns of the DataFrame, broadcasting down the rows:
```python
frame - series
# 			b    d    e
# Utah    0.0  0.0  0.0
# Ohio    3.0  3.0  3.0
# Texas   6.0  6.0  6.0
# Oregon  9.0  9.0  9.0
```

If an index value is not found in either the DataFrame’s columns or the Series’s index, the objects will be reindexed to form the union:
```python
series2
# b    0
# e    1
# f    2
# dtype: int64

frame + series
# 			b   d     e   f
# Utah    0.0 NaN   3.0 NaN
# Ohio    3.0 NaN   6.0 NaN
# Texas   6.0 NaN   9.0 NaN
# Oregon  9.0 NaN  12.0 NaN
```

If you want to instead broadcast over the columns, matching on the rows, you have to use one of the arithmetic methods and specify to match over the index. For example:
```python
series3
# Utah       1.0
# Ohio       4.0
# Texas      7.0
# Oregon    10.0
# Name: d, dtype: float64

frame.sub(series3, axis="index")
#          	b    d    e
# Utah   -1.0  0.0  1.0
# Ohio   -1.0  0.0  1.0
# Texas  -1.0  0.0  1.0
# Oregon -1.0  0.0  1.0
```

### Function Application

[NumPy ufuncs](./numpy.md#universal-functions) (element-wise array methods) also work with pandas objects. Another frequent operation is applying a function on one-dimensional arrays to each column or row. DataFrame’s apply method does exactly this:
```python
# Same frame as previous section
frame.apply(lambda x: x.mean())
# b    4.5
# d    5.5
# e    6.5
# dtype: float64

# Across columns
frame.apply(lambda x: x.mean(), axis="columns")
# Utah       1.0
# Ohio       4.0
# Texas      7.0
# Oregon    10.0
# dtype: float64
```

Many of the most common array statistics (like sum and mean) are DataFrame methods, so using apply is not necessary (as in the example). The function passed to apply need not return a scalar value; it can also return a Series with multiple values:
```python
frame.apply(lambda x: pd.Series([x.mean()], index=["mean"]))
# 		  b	  d	  e
# mean	4.5	5.5	6.5
```

Instead row/column-wise you can do element-wise arithmetic with the `.applymap()` method.

### Sorting and Ranking

#### Sorting
You can sort a Series or a DataFrame with the `sort_`* methods. There's `sort_index` and `sort_values` methods, which are pretty self explanatory. The `sort_index` on DataFrames, though, can be used on either axis:
```python
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=["three", "one"], columns=["d", "a", "b", "c"])

frame
#        d  a  b  c
# three  0  1  2  3
# one    4  5  6  7

frame.sort_index()
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3

frame.sort_index(axis="columns")
#        a  b  c  d
# three  1  2  3  0
# one    5  6  7  4
```

With `sort_values`, any missing value will be sorted to the end of the Series or DataFrames, although they can be sorted to the start instead by using the `na_position` option: `frame.sort_values(na_position="first")`.

**DataFrames require the parameter `by` for `sort_values`**, since pandas doesn't know which value to sort by:
```python
frame = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})

frame
#    b  a
# 0  4  0
# 1  7  1
# 2 -3  0
# 3  2  1

frame.sort_values() # TypeError

frame.sort_values("b") # same as frame.sort_values(by="b")
#    b  a
# 2 -3  0
# 3  2  1
# 0  4  0
# 1  7  1

# You can sort by multiple columns as well
frame.sort_values(["a", "b"])
#    b  a
# 2 -3  0
# 0  4  0
# 3  2  1
# 1  7  1
```

There's an optional parameter `ascending`, which is a boolean for whether to sort in ascending order or not.

#### Ranking

Ranking assigns ranks from one through the number of valid data points in an array, starting from the lowest value. If there's a tie, `rank()` assigns each group the mean rank:
```python
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])

obj.rank()
# 0    6.5
# 1    1.0
# 2    6.5
# 3    4.5
# 4    3.0
# 5    2.0
# 6    4.5
# dtype: float64
```

Ranks can also be assigned according to the order in which they’re observed in the data with the `method` parameter: `obj.rank(method="first")`. The method can be any of the values [in this table](https://wesmckinney.com/book/pandas-basics#tbl-table_pandas_rank), not necessarily `"first"`.

And the `ascending` parameter is here as well, just like when sorting.

### Axis Indexes with Duplicate Labels
While many pandas functions (like reindex) require that the labels be unique, it’s not mandatory. The `is_unique` property of the `index` can tell you whether or not its labels are unique: `frame.index.is_unique`.
```python
obj = pd.Series(np.arange(5), index=["a", "a", "b", "b", "c"])

obj.index.is_unique
# False
```
Data selection is one of the main things that behaves differently with duplicates. Indexing a label with multiple entries returns a Series, while single entries return a scalar value:
```python
obj["a"]
# a    0
# a    1
# dtype: int64

obj["c"]
# 4
```
The same logic extends to indexing rows (or columns) in a DataFrame, a repeated index will return a DataFrame and non repeated values will return a Series.

## Computing Descriptive Statistics

Methods like `mean()` and such aggregation (or reduction) methods support, besides de `axis` param already shown, [this options](https://wesmckinney.com/book/pandas-basics#tbl-table_pandas_reduction).

Other methods are accumulations:
```python
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=["a", "b", "c", "d"], columns=["one", "two"])

df.cumsum()
#     one  two
# a  1.40  NaN
# b  8.50 -4.5
# c   NaN  NaN
# d  9.25 -5.8
```
Some methods are neither reductions nor accumulations. `describe` is one such example, producing multiple summary statistics in one shot:
```python
df.describe() 
#             one       two
# count  3.000000  2.000000
# mean   3.083333 -2.900000
# std    3.493685  2.262742
# min    0.750000 -4.500000
# 25%    1.075000 -3.700000
# 50%    1.400000 -2.900000
# 75%    4.250000 -2.100000
# max    7.100000 -1.300000
```

On nonnumeric data, describe produces alternative summary statistics:
```python
obj = pd.Series(["a", "a", "b", "c"] * 4)

obj.describe()
# count     16
# unique     3
# top        a
# freq       8
# dtype: object
```

Besides `describe`, [here is a list](https://wesmckinney.com/book/pandas-basics#tbl-table_descriptive_stats) of some descriptive and summary statistics.

### Correlation and Covariance

The `corr` method of Series computes the correlation of the overlapping, non-NA, aligned-by-index values in two Series. Relatedly, `cov` computes the covariance:

```python
price = pd.read_pickle("examples/price.pkl")	# just some stocks info
volume = pd.read_pickle("examples/volume.pkl")	# for example

price["MSFT"].corr(price["IBM"])
# 0.49976361144151166

price["MSFT"].cov(price["IBM"])
# 8.870655479703549e-05
```

DataFrame’s `corr` and `cov` methods, on the other hand, return a full correlation or covariance matrix as a DataFrame, respectively:
```python
returns.corr()
#           AAPL      GOOG       IBM      MSFT
# AAPL  1.000000  0.407919  0.386817  0.389695
# GOOG  0.407919  1.000000  0.405099  0.465919
# IBM   0.386817  0.405099  1.000000  0.499764
# MSFT  0.389695  0.465919  0.499764  1.000000

returns.cov()
#           AAPL      GOOG       IBM      MSFT
# AAPL  0.000277  0.000107  0.000078  0.000095
# GOOG  0.000107  0.000251  0.000078  0.000108
# IBM   0.000078  0.000078  0.000146  0.000089
# MSFT  0.000095  0.000108  0.000089  0.000215
```

Using DataFrame’s `corrwith` method, you can compute pair-wise correlations between a DataFrame’s columns or rows with another Series or DataFrame. Passing a Series returns a Series with the correlation value computed for each column, while passing a DataFrame computes the correlations of matching column names:
```python
price.corrwith(price["IBM"])
# AAPL    0.386817
# GOOG    0.405099
# IBM     1.000000
# MSFT    0.499764
# dtype: float64

price.corrwith(volume)
# APL   -0.075565
# GOOG   -0.007067
# IBM    -0.204849
# MSFT   -0.092950
# dtype: float64
```
Passing `axis="columns"` does things row-by-row instead.

### Unique Values, Value Counts, and Membership

This section is quite short and concise so no need for summarizing, just [read here](https://wesmckinney.com/book/pandas-basics#pandas_unique_value_counts).

## Data Loading, Storage, and File Formats

**data loading**: Reading data and making it accessible.
**parsing**: interpreting data as tables and different data types.

### Reading and Writing Data in Text Format

[Here is a full list of functions](https://wesmckinney.com/book/accessing-data#tbl-table_parsing_functions) to read data from text and binary files.

Because of how messy data in the real world can be, some of the data loading functions have accumulated a long list of optional arguments over time (`pd.read_csv` has around 50). The [online pandas documentation](https://pandas.pydata.org/docs/) has many examples about how each of these works, so go there for a full explanation and examples of every parameter and function. Or check this [list of frequently used `read_csv` arguments](https://wesmckinney.com/book/accessing-data#tbl-table_read_csv_function)

#### Basic CSV reading

Use `pd.read_csv("examples/csv_file.csv")` to read the file. It will be loaded into a DataFrame with the headers in the file (if the file has no header set the `header` argument to None, and you can specify your own names with the `names` argument):
```python
# csv_file.csv
# a,b,c,d,message
# 1,2,3,4,hello
# 5,6,7,8,world
# 9,10,11,12,foo

# csv_file2.csv
# 1,2,3,4,hello
# 5,6,7,8,world
# 9,10,11,12,foo

pd.read_csv("examples/csv_file.csv")
# 	 a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo

pd.read_csv("examples/csv_file2.csv", header=None)
# 	 0   1   2   3 	     4
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo

pd.read_csv("examples/csv_file2.csv", header=None, names=['a','b','c','d','message'])
# 	 a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo
```

You can also indicate you want the column at index 4 (or named "message") using the `index_col` argument like this:
```python
pd.read_csv("examples/csv_file2.csv", header=None, names=['a','b','c','d','message'], index_col="messages")
#          a   b   c   d
# message               
# hello    1   2   3   4
# world    5   6   7   8
# foo      9  10  11  12
```

In some cases, a table might not have a fixed delimiter, using whitespace or some other pattern to separate fields. In these cases, you can pass a regular expression as a delimiter for `pd.read_csv` with the `sep` argument. This can be expressed by the regular expression `\s+`, so we have then:
```shell
cat examples/csv_file3.txt
A         B         C
aaa -0.264438 -1.026059 -0.619500
bbb  0.927272  0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd -0.871858 -0.348382  1.100491
```
```python
pd.read_csv("examples/csv_file3.txt", sep="\s+")
#             A         B         C
# aaa -0.264438 -1.026059 -0.619500
# bbb  0.927272  0.302904 -0.032399
# ccc -0.264273 -0.386314 -0.217601
# ddd -0.871858 -0.348382  1.100491
```
> [!NOTE]
> Because there was one fewer column name than the number of data rows, pandas takes the first column as the DataFrame’s index.

Missing data is usually either not present (empty string) or marked by some placeholder value. By default, pandas uses a set of commonly occurring placeholders, such as `NA` and `NULL`, but you can specify them with the `na_values` option, which accepts a sequence of strings to add to the default list of strings recognized as missing. You can also disable these default values setting `keep_default_na` to `False`:
```shell
cat examples/csv_file4.txt
# something,a,b,c,d,message
# one,1,2,3,4,NA
# two,5,6,,8,world			<- Note the two consecutive commas
# three,9,10,11,12,foo
```
```python
pd.read_csv("examples/csv_file4.csv")
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     foo


pd.read_csv("examples/csv_file4.csv", na_values=["foo"])
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     NaN

pd.read_csv("examples/csv_file4.csv", keep_default_na=False)
#   something  a   b     c   d message
# 0       one  1   2   3.0   4      NA
# 1       two  5   6         8   world
# 2     three  9  10  11.0  12     foo
```

##### Reading text files in pieces

You can use the `nrows` argument to read only a part of the file, or the `chunksize` argument to specify the size of the chunks you want to read:
```python
pd.read_csv("examples/csv_file4.csv", nrows=2)
#   something  a   b     c   d message
# 0       one  1   2   3.0   4      NA
# 1       two  5   6         8   world

chunker = pd.read_csv("examples/csv_file4.csv", chunksize=1) # chunker is of type <pandas.io.parsers.readers.TextFileReader>
for piece in chunker:
    # do something with the values
```
> [!NOTE]
> TextFileReader is also equipped with a get_chunk method that enables you to read pieces of an arbitrary size.

##### Writing data to text format

Using DataFrame’s to_csv method, we can write the data out to a comma-separated file. Other delimiters can be used with the `sep` parameter:
```python
data = pd.read_csv("examples/csv_file4.csv")

data.to_csv("examples/out.csv")
# ,something,a,b,c,d,message
# 0,one,1,2,3.0,4,
# 1,two,5,6,,8,world
# 2,three,9,10,11.0,12,foo

data.to_csv("examples/out.csv", sep='|')
# |something|a|b|c|d|message
# 0|one|1|2|3.0|4|
# 1|two|5|6||8|world
# 2|three|9|10|11.0|12|foo
```

Missing values appear as empty string but you can change it with the `na_rep` parameter:
```python
data = pd.read_csv("examples/csv_file4.csv")

data.to_csv("examples/out.csv", na_rep="NULL")
# ,something,a,b,c,d,message
# 0,one,1,2,3.0,4,NULL
# 1,two,5,6,NULL,8,world
# 2,three,9,10,11.0,12,foo
```

There are other params, like the `index` and `header` boolean params to save (or not) the index and header to the file. Check [the docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) for all params.

##### Working with Other Delimited Formats

CSV files come in many different flavors. To define a new format with a different delimiter, string quoting convention, or line terminator, we could define a simple subclass of `csv.Dialect` using Python’s built-in `csv` module. And then just read with that same module:
```python
class my_dialect(csv.Dialect):
    lineterminator = "\n"
    delimiter = ";"
    quotechar = '"'					# in case the characters in the file are quoted (unlike prev examples)
    quoting = csv.QUOTE_MINIMAL

reader = csv.reader(f, dialect=my_dialect)
```

Here is a [list of options](https://wesmckinney.com/book/accessing-data#tbl-table_csv_dialect) for a dialect.

#### JSON Data

JSON is very nearly valid Python code (dictionaries) with the exception of its null value `null` and some other nuances (like disallowing trailing commas at the end of lists). There are several Python libraries for reading and writing JSON data, `json` being one of them and it is built into the Python standard library.

To convert a JSON string to Python form, use `json.loads`, and use `json.dumps` to go from a json object to a string:
```python
obj = """
{
 "name": "Wes",
 "cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
              {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
}
"""

result = json.loads(obj)
result
# {'name': 'Wes',
#  'cities_lived': ['Akron', 'Nashville', 'New York', 'San Francisco'],
#  'pet': None,
#  'siblings': [{'name': 'Scott',
#    'age': 34,
#    'hobbies': ['guitars', 'soccer']},
#   {'name': 'Katie', 'age': 42, 'hobbies': ['diving', 'art']}]}

json_string = json.dumps(result)
json_string
# '{"name": "Wes", "cities_lived": ["Akron", "Nashville", "New York", "San
#  Francisco"], "pet": null, "siblings": [{"name": "Scott", "age": 34, "hobbies": [
# "guitars", "soccer"]}, {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}
# ]}'
```

To convert this into a DataFrame is up to you, you can pass a list of dictionaries (which were previously JSON objects) to the DataFrame constructor and select a subset of the data fields or use the pandas built int `read_json` method:
```json
// examples/json_file.json
[
	{"a": 1, "b": 2, "c": 3},
	{"a": 4, "b": 5, "c": 6},
	{"a": 7, "b": 8, "c": 9}
]
```
```python
pd.read_json("examples/json_file.json")
# 	 a  b  c
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
```
If you need to export data from pandas to JSON, one way is to use the to_json methods on Series and DataFrame.

#### XML and HTML

Python has many libraries for reading and writing data in HTML and XML formats.

To install these libraries use: `pip3 install lxml beautifulsoup4 html5lib` (or your preferred package manager).

##### Parsing HTML

Pandas has a built-in function, `read_html`, which uses all of the python libraries previously mentioned to automatically parse **tables** out of HTML files as DataFrame objects.

The `read_html` function has a number of options, but by default it searches for and attempts to parse all tabular data contained within `<table>` tags. The result is a list of DataFrame objects.

##### Parsing XML

You can read the explanation of how it works (with `lxml` library an such) [here](https://wesmckinney.com/book/accessing-data#io_file_formats_xml). But pandas simplifies the process with the `read_xml` function. So just pass the path to your `.xml` file to `read_xml` and the result is a DataFrame.