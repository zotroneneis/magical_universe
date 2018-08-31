# Iterators

Although we need to create more test functions for the other Magical Universe classes, I want to spend a few days on iterators. First of all, what is meant by the term *iteration*? Iteration describes the process of taking an item and looking at each of its components one by one. Any time we use a loop like

```python
for component in item:
    print(component)
```

we use iteration. Two similar terms that you might have encountered are *iterable* and *iterator*:

**Iterable:**     
As explained in [this stackoverflow post](https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration) an *iterable* is an object that we can *iterate over*. In practice this means that the object defines   
a) an ```__iter__()``` method which returns an *iterator*   
b) **or** a ```__getitem__()``` method (note: since we want to talk about iterators and ```__iter__()``` is the preferred way to iterate, I won't mention ```__getitem__()``` in the rest of this post). 
   
**Iterator:**   
An *iterator* is an object with a ```__next__()``` method. We will take a closer look at each of those methods in a minute.   
   
Our goal for this post will be to create our own iterator. Since potions are an important part of the magical world, we will create a ```Potion``` class that supports iteration. So after successfully creating the class such that it supports the iterator protocol, we will be able to do something like this:

```python
for ingredient in potion:
    print(ingredient)
```

So what do we need in order for our ```Potion``` class to work with a ```for``` loop? We have to define an ```__iter__()``` and a ```__next__()``` method! Let's take a closer look at what these two methods are doing and how they are used in a ```for``` loop.


## ```__iter__()``` and ```__next__()```

**1. What is ```__iter__()``` doing?**    

This method simply returns an iterator object. The iterator object can be used to call ```next()``` on it.  
   
**2. What is ```__next__()``` doing?**     

The ```__next__()``` method takes no arguments and always returns the next element of the object. If there are no elements left, ```__next__()``` must raise the ```StopIteration``` exception. Note: iterators don't have to be finite, we could also create an iterator that produces an infinite number of elements.

Note: we can also use ```iter(object)``` and ```next(object)``` instead of ```object.__iter__()``` and ```object.__next__()```. 
   
As a next step we should understand how the two methods are used within a ```for``` loop.

<!-- [Source](https://docs.python.org/dev/howto/functional.html#iterators) -->

## Behind the scenes of a ```for``` loop

So what happens if we loop over an item using a ```for``` loop? As outlined in the [Python docs](https://docs.python.org/3/tutorial/classes.html#iterators) the process has several steps:   

1. The ```for``` statement calls ```iter()``` on the object you want to iterate over. So in our example it would call ```iter(potion)```.   

2. The ```iter()``` method calls ```__iter__()``` on the object. So in our case this would be ```potion.__iter__()```.   

3. Calling ```iter()``` returns an iterator object.   

4. As described earlier, an iterator object implements the ```__next__()``` method. This method accesses the elements of the object we want to iterate over one at a time. So the loop repeatedly calls ```potion.__next__()```. When no more elements are left, ```__next__()``` raises a ```StopIteration``` exception which tells the ```for``` loop to terminate.   

To make things maximally clear, let's translate the ```for``` loop into the individual steps. The ```for``` loop looked like this:

```python
potion = Potion(...)

for ingredient in potion:
    print(ingredient)
```

Using the steps we can translate this into the following statements which give exactly the same result:

```python
potion = Potion(...)
iterator = potion.__iter__()
while True:
    ingredient = potion.__next__()
    print(ingredient)
```

which is equivalent to

```python
potion = Potion(...)
iterator = iter(potion)
while True:
    ingredient = next(potion)
    print(ingredient)
```

## Creating our own iterator

As mentioned already, we need to define the ```iter()``` and ```next()``` methods to add iterator behavior to our class. As outlined in the [docs](https://docs.python.org/3/tutorial/classes.html#iterators) there are basically two ways to create our ```Potions``` class:   
1. We define an ```__iter__()``` method which returns an object with a ```__next__()``` method.     
2. We define both ```__iter__()``` and ```__next__()```. Then ```__iter__()``` can just return ```self```.   
   
For our ```Potions``` class the second version is fine and more readable. So our ```__iter__()``` will just return ```self```. The ```__next__()``` method returns one ingredient after the other, until no ingredients are left. If none are left, ```__next__()``` will raise a ```StopIteration```.

```python
class Potion:
    """ Creates a potion """
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1

        if self.counter == len(self.ingredients):
            raise StopIteration

        return self.ingredients[self.counter]
```

That's it! Now we can create a potion and iterate over its ingredients in a ```for``` loop:

```python
flask_of_remembrance = Potion(['raven eggshells', 'tincture of thyme', 'unicorn tears', 'dried onions',
                                'powdered ginger root'])

for ingredient in flask_of_remembrance:
    print(ingredient)
```



<!-- What is ```iter()``` doing? -->

<!-- The ```iter()``` function takes an arbitrary object as an input and tries to return an iterator. If the object does not support iteration, ```iter()``` will raise a ```TypeError```. -->



