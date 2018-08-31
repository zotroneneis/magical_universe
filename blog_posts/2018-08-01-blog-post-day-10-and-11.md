# Immutable classes, namedtuples

## Tuples
Before looking at namedtuples, we should review what a tuple is. In Python, a tuple is a simple data structure that can be used for grouping arbitrary objects. Important to know is that tuples are *immutable*. That means that once a tuple has been created, it can not be changed anymore.   

We already used tuples in our Magical Universe. For example, we defined the ```pet``` attribute of the ```Pupil``` class to be a tuple:

```python
pet = ('pet_name', 'pet_type')
cleons_pet = ('Cotton', 'owl')
```

The 'pet' tuple has two fields: 'pet_name' and 'pet_type' that can be accessed using their integer index. Once we create a tuple like ```cleons_pet``` we can't change it anymore. For example, running

```python
cleons_pet[0] = 'Twiggles'
```

throws a ```TypeError: 'tuple' object does not support item assignment```.

## Namedtuples
As their name suggests, namedtuples are a variation (or rather extension) of plain tuples. In particular, namedtuples allow us to name the fields of the tuple. This makes it much easier to access the individual fields. Also, it makes our code more readable. In the plain tuple example above, we could access the values stored in the tuple only by using integer indices, as ```cleons_pet[0]``` or ```cleons_pet[1]```. When having only two fields this is not too bad. But with more than three fields things become messy. 

Creating a namedtuple is easy. There are two kinds of namedtuples we can use: ```collections.namedtuple``` or ```typing.NamedTuple```. When using ```collections.namedtuple``` our pet tuple would be defined as follows:

```python
from collections import namedtuple
Pet = namedtuple('Pet', 'pet_name pet_type')
cleons_pet = Pet('Cotton', 'owl')
```

We can access the fields of the namedtuple using the field names or their indices:
```python
name = cleons_pet[0]
# or
name = cleons_pet.pet_name
```

```typing.NamedTuple``` has a slightly different syntax and allows us to specify the type of each field. It also allows us to add methods to the class (although this is possible with collections.namedtuple, too, it's a little more complex):

```python
from typing import NamedTuple

class Pet(NamedTuple):
    pet_name: str
    pet_type: str

    def __repr__(self):
        return f"{self.pet_name}, {self.pet_type}"

cleons_pet = Pet('Cotton', 'owl')
print('cleons_pet: ', cleons_pet)
```

You can read more about ```typing.NamedTuple``` in the [Python docs](https://docs.python.org/3/library/typing.html).

## Death eater class
We don't want our pupils, professors and ghosts to be immutable. A suitable group of people for an immutable class are the death eaters. So let's create a NamedTuple for them!

```python
from typing import NamedTuple

class DarkArmyMember(NamedTuple):
    name: str
    birthyear: str

    @property
    def leader(self):
        lord_odon = DarkArmyMember('Lord Odon', 1971)
        return lord_odon

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, birthyear: {self.birthyear})"
```

From now on we can easily create new death eaters:
```python
keres = DarkArmyMember('Keres Fulford', 1983)
print('keres: ', keres)
print("Leader: ', keres.leader)
```

## Data classes

Note: When using Python 3.7 we can also use [dataclasses](https://docs.python.org/3/library/dataclasses.html) for creating immutable classes! Data classes are discussed in more detail on [day 16 to 18](http://alpopkes.com/posts/2018/08/coding-challenge-day-16-to-18/).


