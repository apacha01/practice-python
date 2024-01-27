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
