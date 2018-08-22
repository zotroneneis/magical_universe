# Types of methods
A class can have three types of methods: instance methods, class methods and static methods.
   
**Instance methods** are the most common type of method. They take at least the parameter *self* as an input. This parameter points towards an instance of the class when the method is called. An instance method can modify both *object state* and *class state* (the latter can be modified through ```self.__class__```).

Our base class already has an instance method:

```python
def says(self, words):
    return f"{self._name} says {words}"
```
   
**Static methods** take neither a *self* nor *cls* parameter as an input. Therefore, they cannot modify neither object state nor class state. Although they are related to the class, they are independent of the other class or instance methods and can only access the data they are provided with.   
      
Let's add a static method to our base class.   

```python
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name, birthyear, sex):
        ...

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Redmond Dalodore', 1939, 'male')

```

We can also add a static method to our ```Pupil``` class. It will tell us whether a certain grade in an exam passes or fails the exam.

```python
class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """
    ...

    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
                'O': True,
                'Ordinary': True,
                'P': True,
                'Passed': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'H': False,
                'Horrible': False,
                }

        return grades.get(grade, False)
```
   
**Class methods** take at least the parameter *cls* as an input. *cls* points towards the *class* - not a particular object instance - when the method is called. Therefore, a class method can only modify *class state* but not *object state*. Still, changing the class state will still affect all instances of the class.    
   
Class and static methods allow a developer to communicate what intention she/he had in mind when implementing the method. For example, using a static method expresses that the method is independent from everything else around it. Also, class methods can be used as **alternative constructors**.   
   
## Class methods as alternative constructors   
   
- In Python a class can only have one constructor (the ```self.__init__()``` method)
- However, we can use ```@classmethod``` to create factory functions
- These factory functions allow us to create class objects that are configured exactly the way we want them
- In this way, they act like additional constructors
   
For example, we probably want to create the main characters of our Magical Universe. Typing all the names and other attributes every time would be very slow. Adding a few class methods allows us to speed up the process. We can create a Cleon constructor as follows:
   
```python
@classmethod
def cleon(cls):
    return cls('Cleon Bery', 2008, 'male', 'House of Courage', 2018, ('Cotton', 'owl'))
```

## All code for today
```python
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Witchcraft and Wizardry
    """

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        
    def says(self, words):
        return f"{self._name} says {words}"

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Redmond Dalodore', 1939, 'male')


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                  'Broomstick Flying': False,
                  'Art': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'Divination': False,
                  'Herbology': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False}

    @classmethod
    def cleon(cls):
        return cls('Cleon Bery', 2008, 'male', 'House of Courage', 2018, ('Cotton', 'owl'))

    @classmethod
    def flynn(cls):
        return cls('Flynn Gibbs', 2008, 'male', 'House of Courage', 2018, ('Twiggles', 'owl'))

    @classmethod
    def cassidy(cls):
        return cls('Cassidy Ambergem', 2007, 'female', 'House of Courage', 2018, ('Ramses', 'cat'))



class Professor(CastleKilmereMember):
  """
  Creates a Castle Kilmere professor
  """

  def __init__(self, name, birthyear, sex, subject, house=None):
      super().__init__(name, birthyear, sex)
      self.subject = subject
      if house is not None:
          self.house = house

    @classmethod
    def mirren(cls):
        return cls('Miranda Mirren', 1963, 'female', 'Transfiguration', 'House of Courage')

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')

    
class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name, birthyear, sex, year_of_death, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house


if __name__ == "__main__":

    bromley = KilmereMember(name='Bromley Huckabee', birthyear=1959)
    cleon = Pupil(name='Cleon Bery', birthyear=2008, house='House of Courage', start_year=2018)
    headmaster = cleon.school_headmaster()

    mirren = Professor.mirren()
    blade = Professor.blade()
    cleon = Pupil.cleon()
    flynn = Pupil.flynn()
    cassidy = Pupil.cassidy()


```



<!-- Today, I digged a little deeper into the ```@property``` decorator, how it is related to the ```property()``` function and how its getter and setter methods work. These two links ([link1](https://www.programiz.com/python-programming/property), [link2](https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work)) were really helpful. Of course, there is also the [official Python docs](https://docs.python.org/3.7/howto/descriptor.html) on the ```property()``` function. -->

<!-- In the Python Tricks book I already learned about the functioning of decorators. I also knew that ```@property``` is a way of creating a read-only property. However, I was curious about its relation to ```property()``` and the setter and getter methods. The most important things I learned: -->

<!-- Creating a read-only property with ```@property``` is just a different way of using the ```property()``` function. So when considering our Cleon Bery classes, using -->

<!-- ``` -->
<!-- @property -->
<!-- def name(self): -->
<!--     return self._name -->
<!-- ``` -->

<!-- Is equivalent to -->
<!-- ``` -->
<!-- def name(self): -->
<!--     return self._name -->

<!-- name = property(name) -->
<!-- ``` -->

<!-- The full signature of the ```property()``` function is ```property(fget=None, fset=None, fdel=None, doc=None) -> property attribute```. ```fget``` is a function for getting the value of the attribute, ```fset``` is a function for setting the value of the attribute and ```fdel``` is a function for deleting the attribute. All these arguments are *optional*. So we can create a property object like we did above. But we can add extra "power" to it by specifying a setter, getter and/or deleter -->
<!-- method. For example, we could use the setter method to implement certain constraints on the property value. Let's say we add an attribute about the ELM's (Elementare Level of Magic's) to our Pupil class: -->

<!-- ``` -->
<!-- class Pupil(CastleKilmereMember): -->

<!--     def __init__(self, name:str, birthyear:int, house:str, start_year:int): -->
<!--         ... -->
<!--         self._elms = {'Study of Ancient Runes': False, 'Arithmancy': False, 'Astflynnomy': False, 'Care of Magical Creatures': False, 'Charms': False, 'Defence Against Dark Magic': False, 'Divination': False, 'Herbology': False, 'History of Magic': False, 'Muggle Studies': False, 'Potions': False, 'Transfiguration': False} -->

<!--     @property -->
<!--     def elms(self): -->
<!--         return self._elms -->
<!-- ``` -->

<!-- Now, if we want to update the ELM's of a student passed, we have to make sure that she/he actually passed the exam. Otherwise, the ELM can't be awarded. Let's implement that using a setter method. -->

<!-- ``` -->
<!--     @elms.setter -->
<!--     def elms(self, subject_and_grade): -->

<!--         try: -->
<!--             subject, grade = subject_and_grade -->
<!--         except ValueError: -->
<!--             raise ValueError("Pass and interable with two items: subject and grade") -->

<!--         passed = self.passed(grade) -->

<!--         if not passed: -->
<!--             raise ValueError('The exam was not passed so no ELM was awarded!') -->

<!--         self._elms[subject] = True -->

<!--     @staticmethod -->
<!--     def passed(grade): -->
<!--         grades = {'O': True, 'P': True, 'A':True, 'P': False, 'D': False, 'T': False} -->
<!--         return grades[grade] -->
<!-- ``` -->

<!-- In the next days and weeks I want to keep working on these concepts. My current TO DO list looks as follows: -->
<!-- - Add ```__str__``` and ```_repr__``` methods -->
<!-- - Add class methods -->
<!-- - Add getter and deleter methods for properties -->
<!-- - Incorporate Python's abc module -->
<!-- - Create Exception hierarchy and own exception classes -->

<!-- Let's wrap up what I worked on today: -->
<!-- - Digged deeper into ```@property``` and ```property()``` -->
<!-- - Added ```dict.get()``` method which returns default value if key does not exist -->
<!-- - Used another static method -->
