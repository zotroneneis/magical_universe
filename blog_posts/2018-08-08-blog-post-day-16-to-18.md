# Data classes

Data classes are a feature that is new in Python 3.7. And taking a look at them is definitely worth it!

According to the [PEP](https://www.python.org/dev/peps/pep-0557/) on data classes, they are basically "mutable namedtuples with defaults". We already looked at namedtuples on [day 10 and 11](http://www.alpopkes.com/posts/2018/08/coding-challenge-day-10-and-11/). Namedtuples allow us to create an *immutable class* that primarily stores *values* (i.e. attributes). We used namedtuples for our ```DarkArmyMember``` class (because once you become a member of the dark army there is no way back. Unless, of course, you want to get killed by Lord Odon).    
    
Data classes can do the same things as namedtuples. However, they make it much easier to create a class because a data class implements several useful methods by default. Let's create a data class and see what functionality it includes out of the box. We haven't specified the different houses of the Magical Universe yet so let's change that!

We can create a data class by using the ```@dataclass``` decorator. In case you are not using Python 3.7 you can add data classes to your Python 3.6 installation using ```pip install dataclasses```.

```python
from dataclasses import dataclass

@dataclass
class House:
    name: str
    traits: list
```

We can create an instance of the ```House``` class just as before:

```python
house_of_courage = House('House of Courage',
                       ['bravery', 'nerve', 'courage'])
```

## Default functionality of data classes

When defining the ```House``` class as above, Python automatically adds several [special methods](https://docs.python.org/3/glossary.html#term-special-method) to the class. For example, the class includes a ```__init__()``` that looks like this:

```python
def __init__(self, name: str, traits: list):
    self.name = name
    self.traits = traits
```

That's nice, isn't it? All we had to do is list the attributes our ```House``` class should have. Python took care of the rest! Of course, ```__init__()``` is not the only special method added to the class. For example, Python also added a ```__repr__()``` method to ```House```. So we can run 

```python
print(house_of_courage)
```

and get a nice output right away: ```House(name='House of Courage', traits=['bravery', 'nerve', 'courage'])```. Remember: up to now we had to manually add a ```__repr__()``` method to our classes!   
   
Another example: we can automatically compare objects of the ```House``` class. This usually involves implementing a custom ```__eq__()``` method (which can become quite complex). With data classes, ```__eq__()``` is implemented automatically. Let's test this by creating House of Loyalty.

```python
house_of_loyalty = House('House of Loyalty',
                   ['loyalty', 'fairness', 'patience', 'kindness'])

print(house_of_courage == house_of_loyalty)
print(house_of_courage == house_of_courage)
```

As expected, these two expressions output ```False``` and ```True```. 


## Adding default values

We can easily add default values to the fields of our ```House``` data class. For example, we could add a field named 'founded_in'. 

```python
@dataclass
class House:
    name: str
    traits: list
    founded_in: int = 991
```

## Adding methods

Although data classes typically store mostly values, a data class is still a regular class. Therefore, we can freely add methods to our ```House``` data class:

```python
import datetime

@dataclass
class House:
    name: str
    traits: list
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1
```

## Calling ```@dataclass``` with parameters

So far we have used the ```@dataclass``` decorator without any parameters. This corresponds to using the default values of the parameters. The parameters to ```dataclass()``` are (see [Python docs](https://docs.python.org/3/library/dataclasses.html) for full docstring):    
   
- init: If true (the default), a ```__init__()``` method will be generated   
- repr: If true (the default), a ```__repr__()``` method will be generated   
- eq: If true (the default), an ```__eq__()``` method will be generated   
- order: If true (the default is ```False```), ordering methods will be generated. Ordering methods are: ```__lt__(), __le__(), __gt__()```, and ```__ge__()``` which correspond to the operators ```<, <=, >, >= ```   
- unsafe_hash: If true (the default is ```False```), a ```__hash__()``` method will be generated   
- frozen: If true (the default is ```False```), fields are *frozen* so assigning to fields will raise an exception. We will talk more about this parameter on [day 19](http://www.alpopkes.com/posts/2018/08/coding-challenge-day-19/).     
   
So, for example, we can compare two houses to each other, when setting the ```order``` parameter to ```True```:

```python
import datetime

@dataclass(order=True)
class House:
    name: str
    traits: list
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1
```

Now running ```print(house_of_loyalty < house_of_courage)``` will work and produce the output ```False```. Why False? Because data classes compare objects as if the objects were tuples of their fields. So house_of_loyalty is "larger" than house_of_courage because "C" comes before "L" in the alphabet.


## Full class definition

The full ```House``` class will look as follows: 

```python
@dataclass
class House:
    name: str
    traits: list
    head: Professor
    ghost: Ghost
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1
```

The ```head``` and ```ghost``` field will point towards an instance of the ```Professor``` and ```Ghost``` class. For example, for House of Courage we will create Professor Mirren and the Mocking Knight and reference those when instantiating the ```House``` class. See the [full code for day 16 to 18](https://github.com/zotroneneis/cleon_potter_universe/blob/master/code_per_day/day_16_to_18.py) for details.



## Further reading

Data classes have further functionalities that we haven't discussed yet. If you want to know more about them, consider looking at [PEP 557](https://www.python.org/dev/peps/pep-0557/) or watching the [PyCon 2018 talk on dataclasses](https://www.youtube.com/watch?v=T-TwcmT6Rcw).

