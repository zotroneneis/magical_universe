# Context managers and the ```with``` statement

Similar to decorators, context managers are a concept many people use but only few understand. If you haven't heard of the term 'context manager' before: you probably encountered them already while reading or writing from/to a file using the ```with``` statement. 

The most common use of context managers is the proper *management of resources*. In simple terms this means that we want to make sure that we open, read, write and close files correctly. Before creating our own context manager, let's take a look at the most common use of the ```with``` statement and why the ```with``` statement is so useful.    

## Using ```with``` to open files

In the world of Cleon Bery a lot of communication is done via good old letters. So let's imagine that Cleon wants to write a letter to Bromley asking if he, Flynn and Cassidy can stop by for tea in the afternoon. To do so, we open a file called 'letter.txt' and write a few lines of text to the file:

```python
with open('letter.txt', 'w') as letter:
    letter.write("Hi Bromley! \n"
                 "Can Flynn, Cassidy and I stop by for a tea this afternoon? \n"
                 "Cleon")
```

Internally, this is translated to something like this (details of the full translation can be found [in PEP 343](https://www.python.org/dev/peps/pep-0343/#specification-the-with-statement)):

```python
letter= open('letter.txt', 'w')
try:
    letter.write("Hi Bromley! \n"
                 "Can Flynn, Cassidy and I stop by for a tea this afternoon? \n"
                 "Cleon")
finally:
    letter.close()
```

The ```try ... finally``` statement is the key part: it guarantees that the code in the ```finally``` block is **always executed** no matter what happens in the ```try``` block.


## Why the ```with``` statement is useful

In the ```with``` statement above, the ```open``` keyword opens a file descriptor. As you probably know it's very important that every time you open a file, you also need to close it. Otherwise, when opening too many files, your operating system will throw an error at some point.   
   
By using the ```with``` statement we ensure that the open file descriptor is *closed automatically* after the control flow leaves the context of the ```with``` statement. So even when an exception occurs before the end of the ```with``` block, the opened file will be closed. Also when using a ```return```, ```continue``` or ```break``` statement in the ```with``` block, the file will be closed automatically. We don't have to write ```try ... except ... finally``` blocks ourselves - the ```with``` statement takes care of properly closing the file. This makes sure that we are not *leaking any resources*, i.e. forget to close opened files. 

So in short: the ```with``` statement    
a) Makes code that deals with resources more readable     
b) Ensures that resources are not leaked   
    
If you want to see an example of how context managers are used within Python, take a look at the ```threading.Lock``` class. It can be found [here](https://docs.python.org/3/library/threading.html#lock-objects).

## Creating our own context manager

Let's say we want to create a ```Letter``` class in our Magical Universe that functions as a context manager. This would allows us to create a function called ```write_letter()``` that opens a letter object and writes text to it. So in the end we want to be able to use:

```python
with Letter('lettername.txt', 'w') as letter:
    letter.write(...)
```

To achieve this functionality, our ```Letter``` class needs to contain two methods: ```__enter__()``` and ```__exit__()```. When these methods are implemented, our class follows the context manager protocol and supports the ```with``` statement. More about context managers can be found in the [Python docs](https://docs.python.org/3/library/stdtypes.html#typecontextmanager).   
    
## ```Letter``` class

Creating a context manager is not difficult. Our ```Letter``` class will look as follows:

```python
class Letter:
    def __init__(self, letter_name):
        self.letter_name = letter_name

    def __enter__(self):
        self.letter = open(self.letter_name, 'w')
        return self.letter

    def __exit__(self, exc_type, exc_value, traceback):
        if self.letter:
            self.letter.close()
```

That's it! With a proper implemetation of ```__enter__()``` and ```__exit__()``` our ```Letter``` class supports the ```with``` statement:

```python
with Letter('dear_bromley.txt') as letter:
    letter.write("Hi Bromley! \n"
                 "Can Flynn, Cassidy and I stop by for a tea this afternoon? \n"
                 "Cleon")

```


## Steps of the with statement

You might wonder when exactly ```__enter__()``` and ```__exit__()``` are called and what happens behind the scences when using the ```with``` statement. Therefore, we will take a closer look at the individual steps.

To be more precise: when the ```with``` statement is executed with a single file like 'letter.txt':

1. The ```with``` statement invokes a context manager.
2. The context manager's ```__exit__()``` method is loaded for later use.   
3. The context manager's ```__enter__()``` method is invoked.   
4. The value returned by the ```__enter__()``` method is bound to the identifier in the ```as``` clause of the ```with``` statement (i.e. the return value of ```__enter__()``` is bound to the variable 'letter').   
5. The code in the body of the ```with``` statement is executed (i.e. the ```letter.write(...)``` part).   
6. The context manager's ```__exit__()``` method is invoked **no matter what happened in the code body**.

If an exception occured in the code body, its type, value and traceback are passed as arguments to ```__exit__()```. So we can use ```__exit__()``` to handle those exceptions, for example, we could suppress them.
   
For further details on these steps, take a look at the [Python docs](https://docs.python.org/3/reference/compound_stmts.html#with).


## Writing letters

Currently, our ```Letter``` class is very simple and not doing more than the ```open()``` statement. However, ```Letter``` is a regular class, so we could extend it with all kinds of methods. As long as ```__enter__()``` and ```__exit__()``` are implemented properly, the class will support the ```with``` statement. For example, we could keep track of how many letters have been created so far: 

```python
class Letter:
    total_number_of_letters = 0

    def __init__(self, letter_name):
        self.letter_name = letter_name
        self.__class__.total_number_of_letters += 1

    def __enter__(self):
        self.letter = open(self.letter_name, 'w')
        return self.letter

    def __exit__(self, exc_type, exc_value, traceback):
        if self.letter:
            self.letter.close()
```

As a last step, we will add a ```write_letter()``` method to our ```CastleKilmereMember``` class. This will allow all Castle Kilmere members to write actual letters (even if we can't send them by owl).

```python
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    ...

    def write_letter(self, recipient, content):
        letter_name = f"dear_{recipient}.txt"
        with Letter(letter_name) as l:
            l.write(content)

    ...
```


```python
if __name__ == "__main__":
    cleon = Pupil.cleon()

    letter_content = "Hi Bromley! \nCan Flynn, Cassidy and I stop by for a tea this afternoon? \nCleon"
    cleon.write_letter('Bromley', letter_content)

    print(f"Total number of letter creates so far: {Letter.total_number_of_letters}")
```


## Contextlib.contextmanager

Context managers don't have to be class-based. We could also use the [contextlib module](https://docs.python.org/3/library/contextlib.html) to support the with statement. 


<!-- ## Further reading: -->
<!-- https://dbader.org/blog/python-context-managers-and-with-statement -->
<!-- http://effbot.org/zone/python-with-statement.htm -->
<!-- https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/ -->
<!-- https://docs.python.org/3/reference/datamodel.html#context-managers -->
<!-- https://docs.python.org/3/library/stdtypes.html#typecontextmanager -->

