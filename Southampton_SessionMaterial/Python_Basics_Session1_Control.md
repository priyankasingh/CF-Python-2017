## Conditionals

So what if we want to do something that's dependent on whether a given condition is true? In this lesson, we'll learn how to write code that runs only when certain conditions are true.

We can ask Python to take different actions, depending on a condition, with an if statement:

~~~ {.python}
num = 37
if num > 100:
    print("greater")
else:
    print("not greater")
print("done")
~~~
~~~ {.output}
not greater
done
~~~

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows it is true,
the body of the `if`
(i.e., the lines indented underneath it) are executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:

![Executing a Conditional](../python-flowchart-conditional.svg)

Conditional statements don't have to necessarily include an `else`.
If there isn't one,
Python simply does nothing if the test is false:

~~~ {.python}
num = 53
print("before conditional...")
if num > 100:
    print("53 is greater than 100")
print("...after conditional")
~~~
~~~ {.output}
before conditional...
...after conditional
~~~

We can also chain several tests together using `elif`,
which is short for "else if" as shown in the example code chunk below:

~~~ {.python}
num = -3
    if num > 0:
        print("Sign of a number:",num,"is:",1)
    elif num == 0:
        print("Sign of a number",num,"is:",0)
    else:
        print("Sign of a number",num, "is:",-1)

~~~
~~~ {.output}
sign of a number -3 is:  -1
~~~

The keyword `elif` is short for `else if`, and is useful to avoid excessive indentation. An 
`if ... elif ... elif ...` sequence is a substitute for the `switch` or `case` statements 
found in other languages.

One important thing to notice in the code above is that we use a double equals sign `==` to test for equality
rather than a single equals sign
because the latter is used to mean assignment.
This convention was inherited from C,
and while many other programming languages work the same way,
it does take a bit of getting used to...

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:

~~~ {.python}
if (1 > 0) and (-1 > 0):
    print("both parts are true")
else:
    print("one part is not true")
~~~
~~~ {.output}
one part is not true
~~~

while `or` is true if either part is true:

~~~ {.python}
if (1 < 0) or ('left' < 'right'):
    print("at least one test is true")
~~~
~~~ {.output}
at least one test is true
~~~

In this case,
"either" means "either or both", not "either one or the other but not both".

## Using loops to repeat things

Using the tools we've covered till now, repeating a simple statement many times is tedious. The only item
we can currently repeat easily is printing the exact same message multiple times. For example,

~~~{.python}
print("I love programming in Python!\n"*10)
~~~

will produce the output:

~~~{.output}
I love programming in Python!
I love programming in Python!
I love programming in Python!
I love programming in Python!
I love programming in Python!
I love programming in Python!
I love programming in Python!
I love programming in Python!
I love programming in Python!
I love programming in Python!
~~~
Imagine that we wanted to number this list so that we printed:

~~~{.output}
1. I love programming in Python!
2. I love programming in Python!
3. I love programming in Python!
4. I love programming in Python!
5. I love programming in Python!
6. I love programming in Python!
7. I love programming in Python!
8. I love programming in Python!
9. I love programming in Python!
10. I love programming in Python!
~~~

Now, the times operator `*` is no longer capable of allowing us to produce this output. Fortunately, 
Python provides us with multiple general tools for repetition where we'll simply specify which statements 
we want to be repeated and a way to determine how many times to repeat those statements.

To do that, we'll have to teach the computer how to repeat things.

### Shortcomings of the interpreter

Until now, we've been writing everything directly in the Python interpreter.
It's good for testing small bits of code, and you can write any Python using the interpreter - but you wouldn't want to!
Generally you want to have the option of easily running your Python code later, and you don't want to be retyping all the code or copying and pasting it back in to the interpreter. That would be rubbish.

So, much like what we did with Bash, let's take a look at writing a Python script that stores Python in a file that we can run at our leisure.

## Programs or scripts? {.callout}
 
The Python Software Foundation refers to Python as a 'programming language',
But the Python documentation, us, and many others, refer to Python programs
as 'scripts'. So is Python a scripting language or a programming language?
The answer is YES.

Traditionally, languages are either interpreted (like Bash) or compiled (like 
C). The former type were scripting languages, and the latter were programming
languages. But more recently, the lines are beginning to blur.
 
Python can be both! You can compile Python, but you don't need to.
In addition, Python can fulfil the role of a scripting language in similar
ways to Bash, including that it's source code can be run on a multitude
of supporting platforms without needing to be explicitly compiled. But it
can also go much further, and it's designed so you can pretty much write 
anything with it.

For that reason, it's considered a programming language, but to add to the
confusion, we refer to Python programs generally as scripts!

### Our first Python script!

Suppose we want to print each character in the word "lead" on a line of its own.
One way is to use four `print` statements.

Let's write a simple Python program, using our Nano text editor, like we did
with Bash. Let's start Nano (in a separate terminal or shell) and type the following, saving it in a file called `word_print.py`:

~~~ {.python}
word = 'lead'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
~~~

Notice the file has `.py` at the end - this is a convention that indicates this
is a Python script.

Once you've saved it, we can run it from the command line like this (from another terminal or shell, so we can see both the program and how it runs at once):

~~~ {.bash}
$ python word_print.py
~~~

Here we are asking Python to run our Python script. We should see the following:

~~~ {.output}
l
e
a
d
~~~

But looking at our code again, that's a bad approach for two reasons:

1.  It doesn't scale:
    if we want to print the characters in a string that's hundreds of
    letters long, we'd be better off just typing them in.

2.  It's fragile:
    if we give it a longer string,
    it only prints part of the data,
    and if we give it a shorter one,
    it produces an error because we're asking for characters that don't exist.

We can easily demonstrate the second point by changing our script to the following (just changing the first statement):

~~~ {.python}
word = 'tin'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
~~~

Running it again...

~~~ {.bash}
$ python word_print.py
~~~

...gives us the following:

~~~ {.output}
t
i
n
~~~
~~~ {.error}
Traceback (most recent call last):
  File "loop_test.py", line 6, in <module>
    print(word[3])
IndexError: string index out of range
~~~

Here's a better approach:

~~~ {.python}
word = 'lead'
for char in word:
    print(char)
~~~

~~~
l
e
a
d
~~~

This is shorter---certainly shorter than something that prints every character in a hundred-letter string---and
more robust as well:

~~~ {.python}
word = 'oxygen'
for char in word:
    print(char)
~~~

~~~
o
x
y
g
e
n
~~~

The improved version of code for printing characters uses a `for` loop
to repeat an operation---in this case, printing---once for each thing in a collection.
The general form of a loop is:

~~~ {.python}
for variable in collection:
    do things with variable
~~~

We can call the loop variable anything we 
like, but there must be a colon at the end of the line starting the loop,
and we must indent the body of the loop. Unlike many other languages, there is 
no command to end a loop (e.g. end for); what is indented after the for 
statement belongs to the loop.

The great thing about Python is that the simplicity of how it handles loops
means we can use the same loop structure for handling other types of data, like
lists instead. So with one minor alteration:

~~~ {.python}
word = ['oxygen', 'lead', 'tin']
for char in word:
    print(char)
~~~

~~~
oxygen
lead
tin
~~~

Which is really helpful, and means we don't need to remember a different way to do something else for a loop. Although, our variable names are now a bit misleading!

### So what's happening in a loop?

Let's look at a different program called `count_vowels.py`, with another loop that repeatedly updates a variable:

~~~ {.python}
length = 0
for vowel in 'aeiou':
    length = length + 1
print('There are', length, 'vowels')
~~~

~~~ {.bash}
$ python count_vowels.py
~~~

~~~
There are 5 vowels
~~~

It's worth tracing the execution of this little program step by step.
Since there are five characters in `'aeiou'`,
the statement on line 3 will be executed five times.
The first time around, `length` is zero (the value assigned to it on line 1)
and `vowel` is `'a'`.
The statement adds 1 to the old value of `length`,
producing 1, and updates `length` to refer to that new value.
The next time around,
`vowel` is `'e'` and `length` is 1,
so `length` is updated to be 2.
After three more updates,
`length` is 5;
since there is nothing left in `'aeiou'` for Python to process,
the loop finishes
and the `print` statement on line 4 tells us our final answer.

Note that a loop variable is just a variable that's being used to record progress in a loop.
It still exists after the loop is over,
and we can re-use variables previously defined as loop variables as well:

~~~ {.python}
length = 0
for vowel in 'aeiou':
    length = length + 1
print('There are', length, 'vowels')
print('The last vowel counted was', vowel)
~~~

~~~
There are 5 vowels
The last vowel counted was u
~~~

Note also that finding the length of a string is such a common operation
that Python actually has a built-in function to do it called `len`, which
we can add to the end of our program:

~~~ {.python}
print(len('aeiou'))
~~~

~~~
5
~~~

`len` is much faster than any function we could write ourselves,
and much easier to read than a two-line loop;
it will also give us the length of many other things that we haven't met yet,
so we should always use it when we can.


## From 1 to N {.challenge}

Python has a built-in function called `range` that creates a list of numbers:
`range(3)` produces `[0, 1, 2]`, `range(2, 5)` produces `[2, 3, 4]`.
Using `range`,
write a loop to print the first 3 natural numbers:

~~~ {.python}
 1
 2
 3
~~~

## Computing powers with loops {.challenge}

Exponentiation is built into Python:

~~~ {.python}
print(5 ** 3)
125
~~~

Write a loop that calculates the same result as `5 ** 3` using multiplication (and without exponentiation).

## Reverse a string {.challenge}

Write a loop that takes a string, and produces a new string with the characters in reverse order, so `Newton` becomes `notweN`.
