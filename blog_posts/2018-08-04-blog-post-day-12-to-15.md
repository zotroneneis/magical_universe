# Abstract Base Classes, ABC's

The last days I have been working on a lot of new classes and methods. Since they all belong to the same big concept, I decided to create one big post on the whole topic instead of several small ones. So let's get right into it!

## Abtract Base Classes

Up to now, our Magical Universe has a parent class (```CastleKilmereMember```) and several child classes (```Pupil, Professor```, etc.) that inherit all methods from the parent class. But there are other, more advanced applications where simple inheritance is not sufficient.     
     
Abstract base classes are useful if your application involves a *hierarchy* of classes. In particular, in this hierarchy    
a) It should be impossible to instantiate the base class   
b) All subclasses should have a common base class    
c) All subclasses should implement certain methods defined in the base class    
   
Before jumping to further explanations, let's look at an example.   
   
## The ```Spell``` class
   
In the Cleon Bery world, lots of different types of spells exist. In particular, a spell can belong to one of seven classes. This makes the ```Spell``` class a great application for Python's [abc module](https://docs.python.org/3/library/abc.html). To use an Abstract Base Class, we import Python's abc module and flag the method that MUST be implemented by all subclasses with the decorator ```@abstractmethod```. A spell should have a name, an incantation and a certain effect. Also, each spell subclass will have a defining feature.
   
```python
from abc import ABCMeta, abstractmethod

class Spell(metaclass=ABCMeta):
    """Creates a spell"""
    def __init__(self, name: tr, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect

    @abstractmethod
    def cast(self):
        pass

    @property
    @abstractmethod
    def defining_feature(self):
        pass

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, "
               f"incantation: '{self.incantation}', effect: {self.effect})")
```

Let's test whether we can instantiate the ```Spell``` class.

```python
spell = Spell('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly')
```

As expected, this raises an error: ```TypeError: Can't instantiate abstract class Spell with abstract methods cast, defining_feature```. Great! So let's create a subclass. In case you didn't know: a spell can be either a transfiguration, charm, jinx, hex, curse, counter-spell or healing-spell. The ```Charm``` class might look as follows:

```python
class Charm(Spell):
    def __init__(self, name: str, incantation: str, effect: str,
                  difficulty: str = None, min_year: int = None):
        super(Charm, self).__init__(name, incantation, effect)
        self.difficulty = difficulty
        self.min_year = min_year

    def cast(self):
        print(f"{self.incantation}!")
```

Let's instantiate a charm everyone knows.

```python
charm = Charm('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly', 'simple')
```

Well, this is not working. It raises an error *at instantiation time*: ```TypeError: Can't instantiate abstract class Charm with abstract methods defining_feature```. Why? Because we forgot to implement the ```defining_feature``` method!   
      
This highlights a big advantage of using Abstact Base Classes: if a subclass does not implement all the methods required by the base class, an error is raised at *instantiation time*. When not using abtract base classes, we get an error much later, namely only when calling the missing method. A complete implementation of ```Charm``` should look as follows:

```python
class Charm(Spell):
    """
    Creates a charm  -
    a spell that alters the inherent qualities of an object
    """
    def __init__(self, name: str, incantation: str, effect: str,
                  difficulty: str = None, min_year: int = None):
        super(Charm, self).__init__(name, incantation, effect)
        self.difficulty = difficulty
        self.min_year = min_year

    @property
    def defining_feature(self):
        return ("Alteration of the object's inherent qualities, "
                "that is, its behaviour and capabilities")

    def cast(self):
        print(f"{self.incantation}!")
```

Now

```python
charm = Charm('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly', 'simple')
print(charm)
```

works just fine and prints: ```Charm(Stuporus Ratiato, incantation: 'Stuporus Ratiato', effect: Makes objects fly)```


## How to combine @abstractmethod with other decorators

You might noticed another new thing in the code of ```Spell```: we *stacked* two decorators. When stacking decorators it's important to know that they are applied *from bottom to top*. So calling

```python
@property
@abstractmethod
def defining_feature(self):
    pass
```

is equivalent to ```defining_feature = property(abstractmethod(defining_feature))```. But in which place should ```@abstractmethod``` go when combining it with other decorators? According to the [docs](https://docs.python.org/3/library/abc.html): "When abstractmethod() is applied in combination with other method descriptors, it should be applied as the innermost decorator". So keep that in mind when using additional decorators!

## Further advantages of Abstract Base Classes

Apart from the benefits of abstract base classes we have already discussed, ABC's have other advantages and characteristics that are worth knowing. There is an [excellent blog post](https://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python) on "Why use Abstract Base Classes in Python?" that explains the further functionalities of Python's ABC's in detail. 


## Further extensions of the Magical Universe

When implementing the ```Spell``` class and its subclasses, I made sure that the ```Pupil``` and ```DarkArmyMember``` class got a ```cast_spell``` method. Since our Magical Universe should stay realistic a pupil has to study a spell before she/he is able to perform it. Only members of the House of Ambition would study hexes and curses (i.e. dark magic). Also, only certain spells are taught at certain years. If you are highly intelligent (like Cassidy Ambergem), you might be able to perform a spell earlier than less gifted students.

