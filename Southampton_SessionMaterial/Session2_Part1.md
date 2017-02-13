# Reading, Analysing Data and Usage of Python libraries

## Learning Objectives {.objectives}
*   Write a script to open a data file and print out its contents.
*   Perform some operations on strings to extract desired data from it.
*   Understand the basics of how Python handles objects.
*   Explain what a library is, and what libraries are used for.
*   Load a Python library and use the things it contains.
*   Read tabular data from a file.
*   Select individual values and subsections from data.
*   Perform operations on arrays of data.



So far we've seen how to use and manipulate variables, and how to use loops in a script to process strings.
But let's take a look at a more interesting use case - performing some operations on the data in our CSV data file.

We'll start out by looking at how to read the data file and print
its contents in a script, and then modify our script to perform
some conversions and output that. Along the way, we'll see how we can make our code more understandable to 
others (as well as ourselves, when we might come back to it at a later date).

## Printing contents of a data file

We first need to be able to read in our `Annual mean temperature records 1910-2014` data picked from *Scottish Environment Statistics Online - National Climate Information Centre (Met Office)*.  The data is present in file `CCtemperature.csv`. We will be reading our data from this file, and using a loop, print out each line. Let's write another script called `temp_analysis.py`, and enter the following:

~~~ {.python}
temp_data = open('../data/CCtemperature.csv', 'r')

for line in temp_data:
    print(line)
~~~

Using `open`, we first specify the file we wish to open, and then include how
we want to use that file. If we wanted to open a file to write to, we would use 'w', but in this case, we specify `r` for reading.

In general, we know that a loop will iterate over a collection and set a loop
variable to be each item in that collection. When Python deals with files, it
does something quite helpful in a loop. By specifying `temp_data` as our collection, it reads in a single line at a time from our data file, assigning it to our `line` loop control variable.

We can run our code with:

~~~ {.bash}
$ python temp_analysis.py
~~~

And we get the following output:

~~~
Year,Average surface temperature (degrees Celsius),Differences from 1961-1990 average (degrees Celsius)

1910,6.95,-0.08

1911,7.6,0.57

1912,6.97,-0.06

1913,7.43,0.4

1914,7.36,0.33

1915,6.48,-0.55

1916,6.92,-0.11

1917,6.41,-0.62

1918,6.95,-0.08

1919,6.18,-0.85

1920,7.23,0.2

1921,7.72,0.69

1922,6.43,-0.6

1923,6.65,-0.38

1924,7.01,-0.02

1925,6.88,-0.15

1926,7.31,0.28

1927,6.76,-0.27

1928,6.92,-0.11

1929,6.75,-0.28

1930,6.94,-0.09

1931,6.89,-0.14

1932,7.25,0.22

1933,7.81,0.78

1934,7.69,0.66

1935,7.14,0.11

1936,7.15,0.12

1937,6.99,-0.04

1938,7.74,0.71

1939,7.4,0.37

1940,6.86,-0.17

1941,6.72,-0.31

1942,6.82,-0.21

1943,7.6,0.57

1944,7.22,0.19

1945,7.93,0.9

1946,7.17,0.14

1947,7,-0.03

1948,7.48,0.45

1949,7.95,0.92

1950,6.94,-0.09

1951,6.76,-0.27

1952,6.6,-0.43

1953,7.93,0.9

1954,6.86,-0.17

1955,7.03,0

1956,6.88,-0.15

1957,7.5,0.47

1958,6.93,-0.1

1959,7.88,0.85

1960,7.26,0.23

1961,7.29,0.26

1962,6.59,-0.44

1963,6.4,-0.63

1964,7.18,0.15

1965,6.44,-0.59

1966,6.66,-0.37

1967,7.16,0.13

1968,6.8,-0.23

1969,6.79,-0.24

1970,6.86,-0.17

1971,7.7,0.67

1972,6.98,-0.05

1973,7.14,0.11

1974,7.16,0.13

1975,7.53,0.5

1976,7.45,0.42

1977,6.89,-0.14

1978,6.95,-0.08

1979,6.2,-0.83

1980,7.09,0.06

1981,6.8,-0.23

1982,7.4,0.37

1983,7.51,0.48

1984,7.38,0.35

1985,6.51,-0.52

1986,6.42,-0.61

1987,6.74,-0.29

1988,7.52,0.49

1989,7.67,0.64

1990,7.82,0.79

1991,7.42,0.39

1992,7.32,0.29

1993,6.87,-0.16

1994,7.18,0.15

1995,7.49,0.46

1996,6.95,-0.08

1997,8.04,1.01

1998,7.58,0.55

1999,7.73,0.7

2000,7.6,0.57

2001,7.36,0.33

2002,8.02,0.99

2003,8.21,1.18

2004,8.12,1.09

2005,8.09,1.06

2006,8.23,1.2

2007,8.18,1.15

2008,7.67,0.64

2009,7.84,0.81

2010,6.54,-0.49

2011,8.06,1.03

2012,7.32,0.29

2013,7.52,0.49

2014,8.45,1.42
~~~

Hmmm... but that's not really perfect, since it's also printing out additional
newlines which exist at the end of each line in our data file.
We can remove them by stripping them out, using `rstrip`, a function
that works on strings. We can use it like:

~~~ {.python}
    print(line.rstrip())
~~~

## Python and object orientation - in a nutshell {.callout}
 
So far we've used strings, which are a type of object in Python.
In general, an object is an instance of something called a class.

A class defines how a certain thing can behave, and an object
is then a particular thing that behaves the way its class tells it to.
You can define classes that include properties (like variables, associated
with that class), and methods (like functions, also associated with
that class and can perform operations on them). We can use classes to
define things in the real world.

For example, a car is made up of things like an engine, wheels, windows,
and so forth - these things could be defined as classes. And for
each of these, they would have their own properties and methods. A wheel class
for example, could have diameter and width as properties, and a window
could have size, tint and shape and properties, and assuming it's an 
electric window, it could have up() and down() as methods to raise
and lower the window. A class can have as many properties and methods
as we choose to define for it.

When we define a particular car, we could say it has a single engine,
four wheels and four windows. Each of these would be an object --- an instance
of its class --- each with its own set of properties, which could all
be different. We're taking advantage of the fact that all four
windows and all four wheels will behave the same way, but individually.
Using the down() method on one of the windows would cause
that window to lower, but only that window.

So, in our example, `line` is a String object, an instance of a String class.
And that String class has a defined method called `rstrip()`, which 
removes the trailing newline. There are many other String methods which
are incredibly useful!

So, let's try that out:

~~~ {.python}
temp_data = open('../data/CCtemperature.csv', 'r')

for line in temp_data:
    print(line.rstrip())
~~~

And now we get:

~~~
Year,Average surface temperature (degrees Celsius),Differences from 1961-1990 average (degrees Celsius)
1910,6.95,-0.08
1911,7.6,0.57
1912,6.97,-0.06
1913,7.43,0.4
1914,7.36,0.33
1915,6.48,-0.55
1916,6.92,-0.11
1917,6.41,-0.62
1918,6.95,-0.08
1919,6.18,-0.85
1920,7.23,0.2
1921,7.72,0.69
1922,6.43,-0.6
1923,6.65,-0.38
1924,7.01,-0.02
1925,6.88,-0.15
1926,7.31,0.28
1927,6.76,-0.27
1928,6.92,-0.11
1929,6.75,-0.28
1930,6.94,-0.09
1931,6.89,-0.14
1932,7.25,0.22
1933,7.81,0.78
1934,7.69,0.66
1935,7.14,0.11
1936,7.15,0.12
1937,6.99,-0.04
1938,7.74,0.71
1939,7.4,0.37
1940,6.86,-0.17
1941,6.72,-0.31
1942,6.82,-0.21
1943,7.6,0.57
1944,7.22,0.19
1945,7.93,0.9
1946,7.17,0.14
1947,7,-0.03
1948,7.48,0.45
1949,7.95,0.92
1950,6.94,-0.09
1951,6.76,-0.27
1952,6.6,-0.43
1953,7.93,0.9
1954,6.86,-0.17
1955,7.03,0
1956,6.88,-0.15
1957,7.5,0.47
1958,6.93,-0.1
1959,7.88,0.85
1960,7.26,0.23
1961,7.29,0.26
1962,6.59,-0.44
1963,6.4,-0.63
1964,7.18,0.15
1965,6.44,-0.59
1966,6.66,-0.37
1967,7.16,0.13
1968,6.8,-0.23
1969,6.79,-0.24
1970,6.86,-0.17
1971,7.7,0.67
1972,6.98,-0.05
1973,7.14,0.11
1974,7.16,0.13
1975,7.53,0.5
1976,7.45,0.42
1977,6.89,-0.14
1978,6.95,-0.08
1979,6.2,-0.83
1980,7.09,0.06
1981,6.8,-0.23
1982,7.4,0.37
1983,7.51,0.48
1984,7.38,0.35
1985,6.51,-0.52
1986,6.42,-0.61
1987,6.74,-0.29
1988,7.52,0.49
1989,7.67,0.64
1990,7.82,0.79
1991,7.42,0.39
1992,7.32,0.29
1993,6.87,-0.16
1994,7.18,0.15
1995,7.49,0.46
1996,6.95,-0.08
1997,8.04,1.01
1998,7.58,0.55
1999,7.73,0.7
2000,7.6,0.57
2001,7.36,0.33
2002,8.02,0.99
2003,8.21,1.18
2004,8.12,1.09
2005,8.09,1.06
2006,8.23,1.2
2007,8.18,1.15
2008,7.67,0.64
2009,7.84,0.81
2010,6.54,-0.49
2011,8.06,1.03
2012,7.32,0.29
2013,7.52,0.49
2014,8.45,1.42
~~~

### Selecting and printing out only required part from the data

But we're not being very discriminating with our data, we're just blindly
printing out everything. Since we need to process the individual column
that represents the average surface temperature, the 2nd one, how do we extract it from the line of data?

As luck (or more likely, good design) would have it, there's a handy string method called `split()` which can separate all the columns into a list.

We've seen how we can trim trailing newlines from strings with `rstrip()` acting on a string object. Well, we use `split()` in exactly the same way:

~~~ {.python}
    data = line.split(',')
~~~

Although in this case, we're capturing the returned list from `split()` into a 
variable called `data`. We can access elements in that list as before.

So, let's change our code accordingly:

~~~ {.python}
temp_data = open('../data/CCtemperature.csv', 'r')

for line in temp_data:
    data = line.split(',')

    # print 2nd column (average surface temperature)
    print('Avg temperature', data[1])
~~~

Now, it's important to remember that the column we want, the average surface 
temperature, is the 2nd column. But in Python list indexes start at 0, so in 
fact we need to obtain the value from `data[1]` and **not** `data[2]`. So, we 
have made a note to that effect in a *comment*.

## How and when should you add a comment? {.callout}

The trick is to keep your audience in mind when writing code --- this could
be someone else in the lab, or perhaps someone in another institution. A
good rule of thumb is to assume that someone will **always** read your code
at a later date, and this includes a future version of yourself. It can be
easy to forget why you did something a particular way in six months time.
 
Which leads to a good point about comments: generally, they should explain
the **why**. In most cases, the code already explains the **how**, so if
something could be considered unclear, add a comment.
 
A [good philosophy on code comments](http://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/) is that **the best kind of comments are 
the ones you don't need**. You should write your code so it's easier to 
understand without comments first, and only add comments when it **cannot**
be made easier to understand.

And we get:

~~~
Avg temperature Average surface temperature (degrees Celsius)
Avg temperature 6.95
Avg temperature 7.6
Avg temperature 6.97
Avg temperature 7.43
Avg temperature 7.36
Avg temperature 6.48
Avg temperature 6.92
Avg temperature 6.41
Avg temperature 6.95
Avg temperature 6.18
Avg temperature 7.23
Avg temperature 7.72
Avg temperature 6.43
Avg temperature 6.65
Avg temperature 7.01
Avg temperature 6.88
Avg temperature 7.31
Avg temperature 6.76
Avg temperature 6.92
Avg temperature 6.75
Avg temperature 6.94
Avg temperature 6.89
Avg temperature 7.25
Avg temperature 7.81
Avg temperature 7.69
Avg temperature 7.14
Avg temperature 7.15
Avg temperature 6.99
Avg temperature 7.74
Avg temperature 7.4
Avg temperature 6.86
Avg temperature 6.72
Avg temperature 6.82
Avg temperature 7.6
Avg temperature 7.22
Avg temperature 7.93
Avg temperature 7.17
Avg temperature 7
Avg temperature 7.48
Avg temperature 7.95
Avg temperature 6.94
Avg temperature 6.76
Avg temperature 6.6
Avg temperature 7.93
Avg temperature 6.86
Avg temperature 7.03
Avg temperature 6.88
Avg temperature 7.5
Avg temperature 6.93
Avg temperature 7.88
Avg temperature 7.26
Avg temperature 7.29
Avg temperature 6.59
Avg temperature 6.4
Avg temperature 7.18
Avg temperature 6.44
Avg temperature 6.66
Avg temperature 7.16
Avg temperature 6.8
Avg temperature 6.79
Avg temperature 6.86
Avg temperature 7.7
Avg temperature 6.98
Avg temperature 7.14
Avg temperature 7.16
Avg temperature 7.53
Avg temperature 7.45
Avg temperature 6.89
Avg temperature 6.95
Avg temperature 6.2
Avg temperature 7.09
Avg temperature 6.8
Avg temperature 7.4
Avg temperature 7.51
Avg temperature 7.38
Avg temperature 6.51
Avg temperature 6.42
Avg temperature 6.74
Avg temperature 7.52
Avg temperature 7.67
Avg temperature 7.82
Avg temperature 7.42
Avg temperature 7.32
Avg temperature 6.87
Avg temperature 7.18
Avg temperature 7.49
Avg temperature 6.95
Avg temperature 8.04
Avg temperature 7.58
Avg temperature 7.73
Avg temperature 7.6
Avg temperature 7.36
Avg temperature 8.02
Avg temperature 8.21
Avg temperature 8.12
Avg temperature 8.09
Avg temperature 8.23
Avg temperature 8.18
Avg temperature 7.67
Avg temperature 7.84
Avg temperature 6.54
Avg temperature 8.06
Avg temperature 7.32
Avg temperature 7.52
Avg temperature 8.45
~~~

This perhaps isn't what we want - the column header is also part of the output!

## Using Libraries

Words are useful,
but what's more useful are the sentences and stories we build with them.
Similarly,
while a lot of powerful tools are built into languages like Python,
even more live in the libraries they are used to build.

Library is a collection of code (precompiled routines) that a program can use. They are particularly 
useful for storing frequently used routines because you don't need to explicitly link them to every program 
that uses them. Libraries will be automatically looked for routines that are not found elsewhere.

Hence, this session represents an end-to-end scientific Python example, from analysing data (using a library),
to visualisation (using a library).

In order to load our inflammation data,
we need to import a library called NumPy.
In general you should use this library if you want to do fancy things with numbers,
especially if you have matrices.
We can load NumPy using:

~~~ {.python}
import numpy
~~~

Importing a library is like getting a piece of lab equipment out of a storage locker
and setting it up on the bench.
Once it's done,
we can ask the library to read our data file for us:

~~~ {.python}
numpy.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')
~~~
~~~ {.output}
array([[ 0.,  0.,  1., ...,  3.,  0.,  0.],
       [ 0.,  1.,  2., ...,  1.,  0.,  1.],
       [ 0.,  1.,  1., ...,  2.,  1.,  1.],
       ...,
       [ 0.,  1.,  1., ...,  1.,  1.,  1.],
       [ 0.,  0.,  0., ...,  0.,  2.,  0.],
       [ 0.,  0.,  1., ...,  1.,  1.,  0.]])
~~~

The expression `numpy.loadtxt(...)` is a function call that asks Python to run the function `loadtxt` that belongs to the `numpy` library.
This dotted notation is used everywhere in Python
to refer to the parts of things as `thing.component`.

`numpy.loadtxt` has two parameters:
the name of the file we want to read,
and the delimiter that separates values on a line.
These both need to be character strings (or strings for short),
so we put them in quotes.

By default,
only a few rows and columns are shown
(with `...` to omit elements when displaying big arrays).
To save space,
Python displays numbers as `1.` instead of `1.0`
when there's nothing interesting after the decimal point.

Our call to `numpy.loadtxt` read our file,
but didn't save the data in memory.
To do that,
we need to assign the array to a variable.

Just as we can assign a single value to a variable, we can also assign an array of values
to a variable using the same syntax.  Let's re-run `numpy.loadtxt` and save its result:

~~~ {.python}
data = numpy.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')
~~~

This statement doesn't produce any output because assignment doesn't display anything.
If we want to check that our data has been loaded,
we can print the variable's value:

~~~ {.python}
print(data)
~~~
~~~ {.output}
[[ 0.  0.  1. ...,  3.  0.  0.]
 [ 0.  1.  2. ...,  1.  0.  1.]
 [ 0.  1.  1. ...,  2.  1.  1.]
 ...,
 [ 0.  1.  1. ...,  1.  1.  1.]
 [ 0.  0.  0. ...,  0.  2.  0.]
 [ 0.  0.  1. ...,  1.  1.  0.]]
~~~

Now that our data is in memory,
we can start doing things with it.
First,
let's ask what type of thing `data` refers to:

~~~ {.python}
print(type(data))
~~~
~~~ {.output}
<type 'numpy.ndarray'>
~~~

The output tells us that `data` currently refers to an N-dimensional array created by the NumPy library.
We can see what its shape is like this:

~~~ {.python}
print(data.shape)
~~~
~~~ {.output}
(60, 40)
~~~

This tells us that `data` has 60 rows and 40 columns.
`data.shape` is a member of `data`,
i.e.,
a value that is stored as part of a larger value.
We use the same dotted notation for the members of values
that we use for the functions in libraries
because they have the same part-and-whole relationship.

If we want to get a single value from the matrix,
we must provide an index in square brackets,
just as we do in math:

~~~ {.python}
print('first value in data:', data[0, 0])
~~~
~~~ {.output}
first value in data: 0.0
~~~

~~~ {.python}
print('middle value in data:', data[30, 20])
~~~
~~~ {.output}
middle value in data: 13.0
~~~

The expression `data[30, 20]` may not surprise you,
but `data[0, 0]` might.
Programming languages like Fortran and MATLAB start counting at 1,
because that's what human beings have done for thousands of years.
Languages in the C family (including C++, Java, Perl, and Python) count from 0
because that's simpler for computers to do.
As a result,
if we have an M&times;N array in Python,
its indices go from 0 to M-1 on the first axis
and 0 to N-1 on the second.
It takes a bit of getting used to,
but one way to remember the rule is that
the index is how many steps we have to take from the start to get the item we want.

## In the Corner {.callout}

What may also surprise you is that when Python displays an array,
it shows the element with index `[0, 0]` in the upper left corner
rather than the lower left.
This is consistent with the way mathematicians draw matrices,
but different from the Cartesian coordinates.
The indices are (row, column) instead of (column, row) for the same reason,
which can be confusing when plotting data.

An index like `[30, 20]` selects a single element of an array,
but we can select whole sections as well.
For example,
we can select the first ten days (columns) of values
for the first four (rows) patients like this:

~~~ {.python}
print(data[0:4, 0:10])
~~~
~~~ {.output}
[[ 0.  0.  1.  3.  1.  2.  4.  7.  8.  3.]
 [ 0.  1.  2.  1.  2.  1.  3.  2.  2.  6.]
 [ 0.  1.  1.  3.  3.  2.  6.  2.  5.  9.]
 [ 0.  0.  2.  0.  4.  2.  2.  1.  6.  7.]]
~~~

The slice `0:4` means,
"Start at index 0 and go up to, but not including, index 4."
Again,
the up-to-but-not-including takes a bit of getting used to,
but the rule is that the difference between the upper and lower bounds is the number of values in the slice.

We don't have to start slices at 0:

~~~ {.python}
print(data[5:10, 0:10])
~~~
~~~ {.output}
[[ 0.  0.  1.  2.  2.  4.  2.  1.  6.  4.]
 [ 0.  0.  2.  2.  4.  2.  2.  5.  5.  8.]
 [ 0.  0.  1.  2.  3.  1.  2.  3.  5.  3.]
 [ 0.  0.  0.  3.  1.  5.  6.  5.  5.  8.]
 [ 0.  1.  1.  2.  1.  3.  5.  3.  5.  8.]]
~~~

We also don't have to include the upper and lower bound on the slice.
If we don't include the lower bound,
Python uses 0 by default;
if we don't include the upper,
the slice runs to the end of the axis,
and if we don't include either
(i.e., if we just use ':' on its own),
the slice includes everything:

~~~ {.python}
small = data[:3, 36:]
print('small is:')
print(small)
~~~
~~~ {.output}
small is:
[[ 2.  3.  0.  0.]
 [ 1.  1.  0.  1.]
 [ 2.  2.  1.  1.]]
~~~

Arrays also know how to perform common mathematical operations on their values.
The simplest operations with data are arithmetic:
add, subtract, multiply, and divide.
 When you do such operations on arrays,
the operation is done on each individual element of the array.
Thus:

~~~ {.python}
doubledata = data * 2.0
~~~

will create a new array `doubledata`
whose elements have the value of two times the value of the corresponding elements in `data`:

~~~ {.python}
print('original:')
print(data[:3, 36:])
print('doubledata:')
print(doubledata[:3, 36:])
~~~
~~~ {.output}
original:
[[ 2.  3.  0.  0.]
 [ 1.  1.  0.  1.]
 [ 2.  2.  1.  1.]]
doubledata:
[[ 4.  6.  0.  0.]
 [ 2.  2.  0.  2.]
 [ 4.  4.  2.  2.]]
~~~

If,
instead of taking an array and doing arithmetic with a single value (as above)
you did the arithmetic operation with another array of the same size and shape,
the operation will be done on corresponding elements of the two arrays.
Thus:

~~~ {.python}
tripledata = doubledata + data
~~~

will give you an array where `tripledata[0,0]` will equal `doubledata[0,0]` plus `data[0,0]`,
and so on for all other elements of the arrays.

~~~ {.python}
print('tripledata:')
print(tripledata[:3, 36:])
~~~
~~~ {.output}
tripledata:
[[ 6.  9.  0.  0.]
 [ 3.  3.  0.  3.]
 [ 6.  6.  3.  3.]]
~~~

Often, we want to do more than add, subtract, multiply, and divide values of data.
Arrays also know how to do more complex operations on their values.
If we want to find the average inflammation for all patients on all days,
for example,
we can just ask the array for its mean value

~~~ {.python}
print(data.mean())
~~~
~~~ {.output}
6.14875
~~~

`mean` is a method of the array,
i.e.,
a function that belongs to it
in the same way that the member `shape` does.
If variables are nouns, methods are verbs:
they are what the thing in question knows how to do.
This is why `data.shape` doesn't need to be called
(it's just a thing)
but `data.mean()` does
(it's an action).
It is also why we need empty parentheses for `data.mean()`:
even when we're not passing in any parameters,
parentheses are how we tell Python to go and do something for us.

NumPy arrays have lots of useful methods:

~~~ {.python}
print('maximum inflammation:', data.max())
print('minimum inflammation:', data.min())
print('standard deviation:', data.std())
~~~
~~~ {.output}
maximum inflammation: 20.0
minimum inflammation: 0.0
standard deviation: 4.61383319712
~~~

When analyzing data,
though,
we often want to look at partial statistics,
such as the maximum value per patient
or the average value per day.
One way to do this is to select the data we want to create a new temporary array,
then ask it to do the calculation:

~~~ {.python}
patient_0 = data[0, :] # 0 on the first axis, everything on the second
print('maximum inflammation for patient 0:', patient_0.max())
~~~
~~~ {.output}
maximum inflammation for patient 0: 18.0
~~~

We don't actually need to store the row in a variable of its own.
Instead, we can combine the selection and the method call:

~~~ {.python}
print('maximum inflammation for patient 2:', data[2, :].max())
~~~
~~~ {.output}
maximum inflammation for patient 2: 19.0
~~~

What if we need the maximum inflammation for *all* patients,
or the average for each day?
As the diagram below shows,
we want to perform the operation across an axis:

![Operations Across Axes](../python-operations-across-axes.svg)

To support this,
most array methods allow us to specify the axis we want to work on.
If we ask for the average across axis 0,
we get:

~~~ {.python}
print(data.mean(axis=0))
~~~
~~~ {.output}
[  0.           0.45         1.11666667   1.75         2.43333333   3.15
   3.8          3.88333333   5.23333333   5.51666667   5.95         5.9
   8.35         7.73333333   8.36666667   9.5          9.58333333
  10.63333333  11.56666667  12.35        13.25        11.96666667
  11.03333333  10.16666667  10.           8.66666667   9.15         7.25
   7.33333333   6.58333333   6.06666667   5.95         5.11666667   3.6
   3.3          3.56666667   2.48333333   1.5          1.13333333
   0.56666667]
~~~

As a quick check,
we can ask this array what its shape is:

~~~ {.python}
print(data.mean(axis=0).shape)
~~~
~~~ {.output}
(40,)
~~~

The expression `(40,)` tells us we have an N&times;1 vector,
so this is the average inflammation per day for all patients.
If we average across axis 1, we get:

~~~ {.python}
print(data.mean(axis=1))
~~~
~~~ {.output}
[ 5.45   5.425  6.1    5.9    5.55   6.225  5.975  6.65   6.625  6.525
  6.775  5.8    6.225  5.75   5.225  6.3    6.55   5.7    5.85   6.55
  5.775  5.825  6.175  6.1    5.8    6.425  6.05   6.025  6.175  6.55
  6.175  6.35   6.725  6.125  7.075  5.725  5.925  6.15   6.075  5.75
  5.975  5.725  6.3    5.9    6.75   5.925  7.225  6.15   5.95   6.275  5.7
  6.1    6.825  5.975  6.725  5.7    6.25   6.4    7.05   5.9  ]
~~~

which is the average inflammation per patient across all days.

## Thin slices {.challenge}

From our previous topic, the expression `element[3:3]` produces an empty string,
i.e., a string that contains no characters.
If `data` holds our array of patient data,
what does `data[3:3, 4:4]` produce?
What about `data[3:3, :]`?



