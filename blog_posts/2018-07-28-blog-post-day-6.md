# Properties, ```@property``` and ```property()```, setters, getters

Today, I digged a little deeper into the ```@property``` decorator, how it is related to the ```property()``` function and how its getter and setter methods work. These two links ([link1](https://www.programiz.com/python-programming/property), [link2](https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work)) were really helpful. Of course, there is also the [official Python docs](https://docs.python.org/3.7/howto/descriptor.html) on the ```property()``` function.

## The ```@property``` decorator

Yesterday we looked at decorators. The ```@property``` decorator allows us to create a *read-only* property. Let's add a simple property to our CastleKilmereMember class.

```python
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    ...

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear
```

This creates a property called *age* that can be accessed using the dot syntax:   

```python
bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
print(bromley.age)
```

With the current year (2018) this yields the output ```59```. Since the attribute is *read-only* we can't change it:

```python
bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
bromley.age = 44
```

yields an ```AttributeError: can't set attribute```. Of course, we can modify the behavior of ```@property```. Specifically, we can define how a property is accessed, set and deleted by defining its ```getter, setter``` and ```deleter``` methods.


## The relation between ```@property``` and ```property()```

What you should always have in mind when using decorators is their syntax. In particular, remember that

```python
@property
def age(self):
    now = datetime.datetime.now().year
    return now - self.birthyear
```

Is equivalent to
```python
def age(self):
    now = datetime.datetime.now().year
    return now - self.birthyear

age = property(age)
```

The full signature of the ```property()``` function used in the second example (```age = property(age)```) is given by ```property(fget=None, fset=None, fdel=None, doc=None) -> property attribute```.   
- ```fget``` is a function for getting the value of the attribute   
- ```fset``` is a function for setting the value of the attribute   
- ```fdel``` is a function for deleting the attribute   
   
All these arguments are *optional*. So we can create a property object like we did above. But we can add extra "power" to it by specifying a setter, getter and/or deleter
method. For example, we could use the setter method to implement certain constraints on the property value. Let's say we add an attribute about the ELM's (Elementare Level of Magic's) to our Pupil class:

```python
class Pupil(CastleKilmereMember):

    def __init__(self, name: str, birthyear: int, house: str, start_year: int):
        ...
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

    @property
    def elms(self):
        return self._elms
```

Now, if we want to update the ELM's of a student, we have to make sure that she/he actually passed the exam. Otherwise, the ELM can't be awarded. Let's implement that using a setter method.

```python
    @elms.setter
    def elms(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass an iterable with two items: subject and grade")

        passed = self.passed(grade)

        if passed:
            self._elms[subject] = True
        else:
            print('The exam was not passed so no ELM was awarded!')
```

Of course we can also delete the ELM's of a student. But we should probably make sure that the user knows what he is doing when stealing a student all of her/his exams!

```python
    @elms.deleter
    def elms(self):
        print("Caution, you are deleting this students' ELM's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._elms
```
