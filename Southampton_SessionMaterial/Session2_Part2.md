# Modularising your code using functions

## Learning Objectives {.objectives}

*   Define a function that takes parameters.
*   Return a value from a function.
*   Understand the scope of function variables and parameters.
*   Documenting a function.
*   Understand why we should divide programs into small, single-purpose 
    functions.
*   Define and use a module that contains functions.

At this point, we've written some scripts to do various things, including one to 
loop through a data file and output its contents.
But it's not hard to imagine our code getting more complicated as we add
more features.

We'll see how we can amend our code to be better structured to further increase its readability, as well as its maintainability and reuse in other applications.

### Converting from Celsius to Fahrenheit 

Let's look at adding a feature to our code to perform a conversion 
from Celsius to Fahrenheit on the surface temperature data we are looking at:

~~~ {.python}
fahr = ((data[1]  * (9/5)) + 32
~~~

Now this wouldn't work as it is - we can't just apply this formula directly to 
`data[1]` since it's a string. We need to convert it to a number first. To be 
specific, a floating point number.

Fortunately, Python has some built-in functions to do these `type` conversions:

~~~ {.python}
temp_data = open('../data/Updated_CCtemperature.csv', 'r')

for line in temp_data:
     data = line.split(',')

     if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
         pass
     else:
         # extract our average surface temperature in celsius - 2nd column
         celsius = float(data[1])

         # apply standard Celsius to Fahrenheit formula
         fahr = (celsius * 9/5) + 32

         print('Average surface temperature in Fahrenheit', fahr)
~~~

So we first convert our `data[1]` value to a floating point number using 
`float()`, then we are free to use it in our conversion formula. Depending on 
the structure of your own data, you may find you end up doing this a lot!

So now we get:

~~~
Average surface temperature in Fahrenheit 44.510000000000005
Average surface temperature in Fahrenheit 45.68
Average surface temperature in Fahrenheit 44.546
Average surface temperature in Fahrenheit 45.374
Average surface temperature in Fahrenheit 45.248000000000005
Average surface temperature in Fahrenheit 43.664
Average surface temperature in Fahrenheit 44.456
Average surface temperature in Fahrenheit 43.538
Average surface temperature in Fahrenheit 44.510000000000005
Average surface temperature in Fahrenheit 43.123999999999995
Average surface temperature in Fahrenheit 45.014
Average surface temperature in Fahrenheit 45.896
Average surface temperature in Fahrenheit 43.574
Average surface temperature in Fahrenheit 43.97
Average surface temperature in Fahrenheit 44.617999999999995
Average surface temperature in Fahrenheit 44.384
Average surface temperature in Fahrenheit 45.158
Average surface temperature in Fahrenheit 44.168
Average surface temperature in Fahrenheit 44.456
Average surface temperature in Fahrenheit 44.15
Average surface temperature in Fahrenheit 44.492000000000004
Average surface temperature in Fahrenheit 44.402
Average surface temperature in Fahrenheit 45.05
Average surface temperature in Fahrenheit 46.058
Average surface temperature in Fahrenheit 45.842
Average surface temperature in Fahrenheit 44.852
Average surface temperature in Fahrenheit 44.870000000000005
Average surface temperature in Fahrenheit 44.582
Average surface temperature in Fahrenheit 45.932
Average surface temperature in Fahrenheit 45.32
Average surface temperature in Fahrenheit 44.348
Average surface temperature in Fahrenheit 44.096000000000004
Average surface temperature in Fahrenheit 44.275999999999996
Average surface temperature in Fahrenheit 45.68
Average surface temperature in Fahrenheit 44.996
Average surface temperature in Fahrenheit 46.274
Average surface temperature in Fahrenheit 44.906
Average surface temperature in Fahrenheit 44.6
Average surface temperature in Fahrenheit 45.464
Average surface temperature in Fahrenheit 46.31
Average surface temperature in Fahrenheit 44.492000000000004
Average surface temperature in Fahrenheit 44.168
Average surface temperature in Fahrenheit 43.879999999999995
Average surface temperature in Fahrenheit 46.274
Average surface temperature in Fahrenheit 44.348
Average surface temperature in Fahrenheit 44.653999999999996
Average surface temperature in Fahrenheit 44.384
Average surface temperature in Fahrenheit 45.5
Average surface temperature in Fahrenheit 44.474000000000004
Average surface temperature in Fahrenheit 46.184
Average surface temperature in Fahrenheit 45.068
Average surface temperature in Fahrenheit 45.122
Average surface temperature in Fahrenheit 43.862
Average surface temperature in Fahrenheit 43.519999999999996
Average surface temperature in Fahrenheit 44.924
Average surface temperature in Fahrenheit 43.592
Average surface temperature in Fahrenheit 43.988
Average surface temperature in Fahrenheit 44.888
Average surface temperature in Fahrenheit 44.239999999999995
Average surface temperature in Fahrenheit 44.222
Average surface temperature in Fahrenheit 44.348
Average surface temperature in Fahrenheit 45.86
Average surface temperature in Fahrenheit 44.564
Average surface temperature in Fahrenheit 44.852
Average surface temperature in Fahrenheit 44.888
Average surface temperature in Fahrenheit 45.554
Average surface temperature in Fahrenheit 45.41
Average surface temperature in Fahrenheit 44.402
Average surface temperature in Fahrenheit 44.510000000000005
Average surface temperature in Fahrenheit 43.16
Average surface temperature in Fahrenheit 44.762
Average surface temperature in Fahrenheit 44.239999999999995
Average surface temperature in Fahrenheit 45.32
Average surface temperature in Fahrenheit 45.518
Average surface temperature in Fahrenheit 45.284
Average surface temperature in Fahrenheit 43.718
Average surface temperature in Fahrenheit 43.556
Average surface temperature in Fahrenheit 44.132000000000005
Average surface temperature in Fahrenheit 45.536
Average surface temperature in Fahrenheit 45.806
Average surface temperature in Fahrenheit 46.076
Average surface temperature in Fahrenheit 45.356
Average surface temperature in Fahrenheit 45.176
Average surface temperature in Fahrenheit 44.366
Average surface temperature in Fahrenheit 44.924
Average surface temperature in Fahrenheit 45.482
Average surface temperature in Fahrenheit 44.510000000000005
Average surface temperature in Fahrenheit 46.471999999999994
Average surface temperature in Fahrenheit 45.644
Average surface temperature in Fahrenheit 45.914
Average surface temperature in Fahrenheit 45.68
Average surface temperature in Fahrenheit 45.248000000000005
Average surface temperature in Fahrenheit 46.436
Average surface temperature in Fahrenheit 46.778000000000006
Average surface temperature in Fahrenheit 46.616
Average surface temperature in Fahrenheit 46.562
Average surface temperature in Fahrenheit 46.814
Average surface temperature in Fahrenheit 46.724000000000004
Average surface temperature in Fahrenheit 45.806
Average surface temperature in Fahrenheit 46.112
Average surface temperature in Fahrenheit 43.772
Average surface temperature in Fahrenheit 46.508
Average surface temperature in Fahrenheit 45.176
Average surface temperature in Fahrenheit 45.536
Average surface temperature in Fahrenheit 47.21
~~~

### Modularising conversion code into a function

Whilst this is a simple calculation, there are many things we may want to do that are more complex. What is essentially a single task may require a number of lines of code to accomplish it, and with many of these our code could become quite messy.

We'd also like a way to package our code so that it is easier to reuse,
and Python provides for this by letting us define things called 'functions' -
a shorthand way of re-executing longer pieces of code.

~~~ {.python}
temp_data = open('../data/Updated_CCtemperature.csv', 'r')

def celsius_to_fahr(celsius):
    # apply standard Celsius to Fahrenheit formula
    fahr = (celsius * 9/5) + 32 
    return fahr

for line in temp_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our avg surface temperature in celsius - 2nd column
        celsius = float(data[1])

        fahr = celsius_to_fahr(celsius)

        print('Avg surface temperature in Fahrenheit', fahr)
~~~

The definition opens with the word `def`,
which is followed by the name of the function
and a parenthesised list of parameter names.
The body of the function --- the
statements that are executed when it runs --- is indented below the definition line,
typically by four spaces.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a return statement to send a result back to whoever asked for it.

## How large should functions be? {.callout}
 
We use functions to define a big task in terms of smaller ones. This helps 
to make our code more readable, as well as allowing us to more easily
reuse and maintain that code.
 
The trick when writing functions is to ensure they don't themselves become
unmanageable, and it's very easy to write large functions. So when your
function starts getting large, consider decomposing it further into separate 
functions. There's no hard and fast rule for when a function is too 'large'
--- some say 15-20 lines, some say no more than a page long. But in general,
think about how complex it is to understand, generally how readable
it is, and whether it would benefit from splitting up into more functions.

Note that the function is at the top of the script. This is because Python
reads the script from top to bottom, and if we called the function before we
defined it, Python wouldn't know about it and throw an error like this:

~~~
Traceback (most recent call last):
  File "temp_analysis.py", line 13, in <module>
    fahr = celsius_to_fahr(celsius)
NameError: name 'celsius_to_fahr' is not defined
~~~

And when we run it again --- which we most definitely should, to make sure it's still working as expected --- we see the same output, which is correct.

## How do function parameters work? {.challenge}
 
We actually used the same variable name `celsius` in our main code and
and the function. But it's important to note that even though they
share the same name, they don't refer to the same thing. This is
because of variable **scoping**.
 
Within a function, any variables that are created (such as parameters 
or other variables), only exist within the **scope** of the function.
 
For example, what would be the output from the following:
 
~~~ {.python}
f = 0
k = 0

def multiply_by_10(f):
      k = f * 10
      return k

multiply_by_10(2)
multiply_by_10(8)

print(k)
~~~

1. 20
2. 80
3. 0
 
This is really useful, since it means we don't have to worry about
conflicts with variable names that are defined outside of our function
that may cause it to behave incorrectly.

## Combining strings {.challenge}

"Adding" two strings produces their concatenation:
`'a' + 'b'` is `'ab'`.
Write a function called `fence` that takes two parameters called `original` and `wrapper`
and returns a new string that has the wrapper character at the beginning and end of the original.
A call to your function should look like this:

~~~ {.python}
print(fence('name', '*'))
*name*
~~~

## Palindrome String check {.challenge}

A "Palindrome" is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
Write a function (any name of your choice) that takes `input_string` as a parameter
and returns either `True` or `False` based on whether the input string is a palindrome or not respectively. 
Try to make it case insensitive.  
Following the function definition, a call to your function should look like this:

~~~{.python}
is_palindrome("hello")
False
is_palindrome("Deed")
True
~~~

## Performing more temperature conversions

Of course, we can also add more functions. Let's add another, which performs
a conversion from Fahrenheit to Kelvin. The formula looks like this:

~~~ {.python}
kelvin = ((fahr - 32) * (5/9)) + 273.15
~~~

Now, we could just add a new function that does this exact conversion. But
Kelvin uses the same units as Celsius, the part of the formula that
converts to Celsius units is the same. We could just used our `fahr_to_celsius`
function for the unit conversion, and add 273.15 to that to get Kelvin. So
our new function becomes:

~~~ {.python}
def fahr_to_kelvin(fahr):
    # apply standard Fahrenheit to Kelvin formula
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin
~~~

Which we insert after the `fahr_to_celsius` function (since our new function
needs to call that one). We can then amend our code to also call that new
function and output the result. Our code then becomes:

~~~ {.python}
temp_data = open('../data/Updated_temp_fahr.csv', 'r')

def fahr_to_celsius(fahr):
    # apply standard Fahrenheit to Celsius formula
    celsius = ((fahr - 32) * (5/9)) 
    return celsius

def fahr_to_kelvin(fahr):
    # apply standard Fahrenheit to Kelvin formula
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin

for line in temp_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our average surface temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = fahr_to_celsius(fahr)
        kelvin = fahr_to_kelvin(fahr)

        print('Avg surface temperature in Celsius', celsius, 'Kelvin', kelvin)
~~~

Hmm... our code is starting to get a little large with these functions.
What could we do to make it clearer and less cluttered?

### Modularising conversion code into a library

Words are useful,
but what's more useful are the sentences and stories we build with them.
Similarly,
while a lot of powerful tools are built into languages like Python,
even more live in the libraries they are used to build.

A library is a collection of code (precompiled routines, functions) that a program can use. They are particularly 
useful for storing frequently used routines because you don't need to explicitly link them to every program 
that uses them. Libraries will be automatically looked for routines that are not found elsewhere.

So we can go one step further to improve the structure of our
code. We can separate out the two functions and have them in a separate
Python module (or library) which we can use.

Create a new file called 
`temp_conversion.py` and copy and paste those two functions into it, then 
save it, and remove those functions from the original `climate_analysis.py` 
script and save that. We'll see how to use those library functions 
shortly. But first, let's take this opportunity to improve our 
documentation of those functions!

The usual way to put documentation in software is to add comments, as
we've already seen. But when describing functions, there's a better way.
If the first thing in a function is a string that isn't assigned to a variable,
that string is attached to the function as its documentation:

~~~ {.python}
"""A library to perform temperature conversions"""

def fahr_to_celsius(fahr):
    """Convert Fahrenheit to Celsius.

    Uses standard Fahrenheit to Celsius formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    celsius = ((fahr - 32) * (5/9)) 
    return celsius

def fahr_to_kelvin(fahr):
    """Convert Fahrenheit to Kelvin.

    Uses standard Fahrenheit to Kelvin formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin
~~~

A string like this is called a docstring.
We don't need to use triple quotes when we write one,
but if we do, we can break the string across multiple lines. This also
applies to modules

So how would we use this module and its functions in code?
We do this by `import`ing the module into Python.

~~~ {.python}
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import temp_conversion
~~~

When modules and functions are described in docstrings, we can ask for these 
explanations directly from the interpreter which can be useful. Following on
from the above:

~~~ {.python}
>>> help(temp_conversion)
~~~

So here's the help we get for the module:

~~~
Help on module temp_conversion:

NAME
    temp_conversion - A library to perform temperature conversions

FUNCTIONS
    fahr_to_celsius(fahr)
        Convert Fahrenheit to Celsius.
        
        Uses standard Fahrenheit to Celsius formula
        
        Arguments:
        fahr -- the temperature in Fahrenheit
    
    fahr_to_kelvin(fahr)
        Convert Fahrenheight to Kelvin.
        
        Uses standard Fahrenheit to Kelvin formula
        
        Arguments:
        fahr -- the temperature in Fahrenheit

FILE
    /Users/user/Desktop/Disk Image New Installs/CodeFirst- Teaching/Spring 2016 Python Teaching/Southampton_SessionMaterial/Codes/temp_conversion.py
~~~

Here, note we've used the term `library` in the code documentation. This
is a more conventional, general term for a set of routines in any language.

Similarly, for Docstrings in functions, e.g.:

~~~ {.python}
>>> help(temp_conversion.fahr_to_celsius)
~~~

Note that we need to put in `temp_conversion.` prior the function name. We need
to do this to specify that the function we want help on is within the
`temp_conversion` module.

So we get:

~~~
Help on function fahr_to_celsius in module temp_conversion:

fahr_to_celsius(fahr)
    Convert Fahrenheit to Celsius.
    
    Uses standard fahrenheit to Celsius formula
    
    Arguments:
    fahr -- the temperature in Fahrenheit
~~~

And then we need to `import` that function from our module into our script, so 
we can use it.

~~~ {.python}
import temp_conversion

temp_data = open('../data/Updated_temp_fahr.csv', 'r')

for line in temp_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our avg surface temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = temp_conversion.fahr_to_celsius(fahr)
        kelvin = temp_conversion.fahr_to_kelvin(fahr)

        print('Avg Surface temperature in Celsius', celsius, 'Kelvin', kelvin)
~~~

Like when we used the interpreter to ask for help on the `fahr_to_celsius()`
function, we need to prefix the function with its `temp_conversion` module name.

Again, the results should be the same as before.




